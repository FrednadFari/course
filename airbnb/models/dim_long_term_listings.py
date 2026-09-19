def model(dbt, session):
    lisitngs = dbt.ref( "dim_listings_cleansed")

    return (lisitngs.filter(lisitngs["MINIMUM_NIGHTS"] >= 30)
        .select("LISTING_ID", "LISTING_NAME", "PRICE"))