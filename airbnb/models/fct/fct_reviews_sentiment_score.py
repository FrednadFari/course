# <fact_reviews> as input, | sentiment_score | 
# -1->negative, 0->neutral, 1->posistive
# used library textblob, Description: python NLP library built on NLTK, 
#   -use case-> for simple setiment analysis.

from snowflake.snowpark.functions import udf
from snowflake.snowpark.types import StringType
from textblob import TextBlob

def model(dbt, session):
    dbt.config(
        materialized="table",
        packages=["textblob"]
    )

    # Load input-table<fact_reviews>
    df = dbt.ref("fct_reviews")

    # @udf(return_type=StringType(), input_types=[StringType()])
    @udf(
        return_type=StringType(),
        input_types=[StringType()],
        packages=["textblob"],
    )
    def get_sentiment(text: str) -> str:
        polarity = TextBlob(text).sentiment.polarity
        if polarity > 0:
            return "positive"
        elif polarity < 0:
            return "negative"
        return "neutral"

    df = df.with_column("REVIEW_SENTIMENT", get_sentiment(df["REVIEW_TEXT"]))

    return df