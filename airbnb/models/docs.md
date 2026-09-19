{% docs dim_listing_cleansed_minimum_nights %}
Minimum number of nights required to rent this property.

keep in mind that old listings might have 'minimum_nights' set to 0 in the source tables. Our cleansed algorithm updates this ot '1'.
{% enddocs %}

{% docs dim_hosts_cleansed_overview %}
# dim_hosts_cleansed
Cleansed table of Airbnb hosts.

![dim_hosts_cleansed structure](assets/dim_hosts_cleansed.png)
{% enddocs %}