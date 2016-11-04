from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.IntegerField):

    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:

            try:
                query_set = self.model.objects.all()

                if self.for_fields:
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    query_set = query_set.filter(**query)
                    last_item = query_set.latest(self.attname)
                    value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)
