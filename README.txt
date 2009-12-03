Provides a django template tag to be used with the django-flash package. The
tag retrieves all flash messages and removes them. This prevents the issue of
having flash messages "stick around" too often. For example, when displaying a
flash message on user error. There's typically no redirect in this case, so the
flash message stays around for two requests.

What's returned from the template tag is a dictionary with the items from the
request.flash object.

Example template use, assuming keys are message types (ie error/info) and
values are the list of messages for that type:

{% load flash_messages %}
{% get_and_remove_flash_messages as flash_messages %}
{% if flash_messages %}
  {% for msg_type, messages in flash_messages.items %}
    <ul>
      {% for message in messages %}
        <li>{{ message|safe }}</li>
      {% endfor %}
    </ul>
  {% endfor %}
{% endif %}
