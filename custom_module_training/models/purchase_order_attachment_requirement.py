from odoo import fields, models


class PurchaseOrderAttachmentRequirement(models.Model):
    _name = "purchase.order.attachment.requirement"
    _description = "Purchase Order Attachment Requirement"

    name = fields.Char()
    document_type = fields.Selection(
        [
            ("material", "Material"),
            ("service", "Service"),
            ("both", "Both"),
            ("other", "Other"),
        ],
        index=True,
    )
    document_count = fields.Integer()
    is_mandatory = fields.Boolean()
