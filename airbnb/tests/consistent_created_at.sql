-- singular-test >> new-item -itemtype file -path "tests/consistent_created_at.sql"
-- tasks: there is no review data in "fct_reviews.review_date" which submitted before
-- logic: joining two tables and test them with 
-- datatype check>> WHERE TO_DATE(r.review_date) < TO_DATE(l.created_at)

SELECT 
    r.listing_id,
    r.review_date,
    l.created_at
FROM {{ref('fct_reviews')}} AS r 
INNER JOIN {{ref('dim_listings_cleansed')}} AS l 
    ON r.listing_id = l.listing_id
WHERE r.review_date < l.created_at