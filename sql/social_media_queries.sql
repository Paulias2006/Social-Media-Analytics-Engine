-- Portfolio SQL queries for social media analytics.

-- 1. Engagement by platform
SELECT
    platform,
    COUNT(*) AS posts,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate,
    ROUND(SUM(reach), 0) AS total_reach
FROM posts
GROUP BY platform
ORDER BY avg_engagement_rate DESC;

-- 2. Topic performance
SELECT
    topic,
    COUNT(*) AS posts,
    ROUND(SUM(likes + comments + shares + saves), 0) AS total_engagements,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate
FROM posts
GROUP BY topic
ORDER BY total_engagements DESC;

-- 3. Sentiment and engagement
SELECT
    sentiment_label,
    COUNT(*) AS posts,
    ROUND(AVG(reach), 2) AS avg_reach,
    ROUND(AVG(engagement_rate), 2) AS avg_engagement_rate
FROM posts
GROUP BY sentiment_label
ORDER BY posts DESC;

-- 4. Top posts to review
SELECT
    post_id,
    published_date,
    platform,
    topic,
    content_type,
    sentiment_label,
    reach,
    engagement_rate
FROM posts
ORDER BY engagement_rate DESC
LIMIT 20;
