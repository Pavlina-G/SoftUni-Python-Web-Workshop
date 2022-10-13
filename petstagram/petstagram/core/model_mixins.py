class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        return ', '.join(f'{str_field}={getattr(self, str_field, None)}' for str_field in self.str_fields)
        # return '; '.join(
        #     f'{f}={self.__dict__[f]}' for f in self.str_fields
        # )

