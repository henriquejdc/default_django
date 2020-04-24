from django.utils.translation import ugettext_lazy as _
from livesettings.functions import config_register
from livesettings.values import ConfigurationGroup, PositiveIntegerValue, MultipleStringValue


# Config group to hold all the configs
MYAPP_GROUP = ConfigurationGroup('PRODUCT', _('My App Settings'), ordering=0)

# When ordering parameter is not passed, all inputs are sorted by name
config_register(PositiveIntegerValue(
    MYAPP_GROUP,
    'NUM_DISPLAY',
    description=_('Numero de produtos para aparecer na home'),
    help_text=_("Numero de produtos ao aparecer na home"),
    # if no help_text is given, Default falue is displayed
    default=5
))

# Another example of allowing the user to select from several values
config_register(MultipleStringValue(
    MYAPP_GROUP,
    'RANDOM_FEATURED',
    description=_("Measurement System"),
    help_text=_("Default measurement system to use."),
    choices=[('metric', _('Metric')),
             ('imperial', _('Imperial'))],
    default="imperial"
))