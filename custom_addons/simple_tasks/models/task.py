from odoo import models, fields, api

# task model - the blueprint for tasks
class SimpleTask(models.Model):

    #table name in the database
    _name = 'simple.task'
    _description = 'Simple Task'

    # FIELDS
    name = fields.Char(
        string = 'Task Name', # Label shown to users
        required = True,
        help = 'Enter the name of the task'
    )

    description = fields.Text(
        string = 'Description',
        help = 'Tell me more about this task'
    )

    is_done = fields.Boolean(
        string = 'Done?',
        default = False, #By default, the task/s are not done
        help = 'Check this when the task is finished'
    )

    priority = fields.Selection(
        [
            ('low', 'Low Priority'),
            ('medium', 'Medium Priority'),
            ('high', 'High Priority'),
        ],
        string = 'Priority',
        default = 'medium'
    )

    assigned_to = fields.Many2one(
        'res.users', #connect to odoo's user model
        string = 'Assigned To',
        help = 'Who should do this task?'
    )

    created_date = fields.Datetime(
        string = 'Created On',
        default = fields.Datetime.now
    )

    task_days_old = fields.Integer(
        string = 'Days Since Created',
        compute = '_compute_days_old',
        help = 'How many days have passed since this task was created'
    )

    #METHODS - Actions you can perform
    def mark_as_done(self):
        '''Mark this task as done'''
        self.is_done = True

    def mark_as_not_done(self):
        '''Mark this task as not done'''
        self.is_done = False

    def reset_priority(self):
        '''Reset the priority to medium'''
        self.priority = 'medium'

    @api.depends('created_data')
    def _compute_days_old(self):
        """
            Calculate how many days old this task is
        """
        for task in self:
            if task.created_date:
                today = fields.Datetime.now()
                difference = today - task.created_date
                task.task_days_old = difference.days
            else:
                task.task_days_old = 0
                