{% macro learn_variables() %}
    {% set your_name_jinja = "FRED" %}
    {{ log("Hello " ~ your_name_jinja, info=True)}}

    {{ log("Hello dbt user-> " ~ var("user_name", "NO USERNAME is set") ~ "!", info=True)}}
{% endmacro %}