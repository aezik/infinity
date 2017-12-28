from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField

from oo.generic.models import (
    GenericTranslationModel
)


class Type(GenericTranslationModel):
    """
    A Type is a snapshot of a definition of a concept by its qualities:

    we often formulate goals with respect to classes of items, however,
    as soon as we conceptualize a class of items distinguished by shared
    qualities of its members, the class itself becomes an item (a Type).

    One could say that Type is like a SELECT statement by qualities, so
    goals could be specified with respect to "Types". For example:

         artificially intelligent systems may target entities that
         behave in certain ways, without even caring about specific
         identities (Instances), only caring about qualities (Type).

    We create and use Types like concepts, to express and define abstract
    goals.

    Types will work like situational "Concept Snapshots" -- just like
    gloassaries help book authors to be precise in their books, the Types
    will help authors of goals to be precise about the *type of things*
    (Instances) we want to exist.

    NOTE: we could use other close approximations, like "Term", "Concept",
    "Word", etc., the choice to use "Type" is chosen to encourage people
    to create them, rather than use existing conceptions. Also, it is
    natural to say "Instance Type", but not so "Instance Term".

    This model will be used to store snapshots of concepts, found in
    various dictionaries and ontologies, that the user will be able to use
    to look up for a type, or create one's own.

    This will also include the concepts, and their labels, where each
    label and definition can be multilingual.
    """
    name = models.TextField()
    definition = models.TextField(null=True, blank=True)

    is_category = models.BooleanField(default=False)


    parents = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='parent_types'
    )

    source = models.TextField(null=True, blank=True)
    data = JSONField(null=True, blank=True)

    def __str__(self):
        return '[{}] {}'.format(self.pk, self.name)

    class Meta:
        translation_fields = (
            ('name', True),
            ('definition', False),
        )
        verbose_name = _("Type")
        verbose_name_plural = _("Types")


class Instance(GenericTranslationModel):
    """
    F: Instances are references to anything with respect to which we
    will formulate goals. To be implemented in blockchain db.
    """
    THING = 0
    AGENT = 1
    PLACE = 2
    EVENT = 3

    ITEM_ROLES = [
        (THING, _('Thing')),
        (AGENT, _('Agent')),
        (PLACE, _('Place')),
        (EVENT, _('Event')),
    ]

    role = models.PositiveSmallIntegerField(ITEM_ROLES, default=THING)
    concept = models.ForeignKey(Type, on_delete=models.CASCADE)

    identifiers = models.TextField()
    description = models.TextField()

    source = models.TextField(null=True, blank=True)
    data = JSONField(null=True, blank=True)

    def __str__(self):
        return '[{}] {}: {}'.format(dict(self.ITEM_ROLES).get(self.role), self.pk, self.identifiers)

    class Meta:
        translation_fields = (
            ('description', False),
        )
        verbose_name = _("Instance")
        verbose_name_plural = _("Instances")

