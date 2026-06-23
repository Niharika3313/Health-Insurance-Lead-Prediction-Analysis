-- How big is our lead funnel? What's our overall conversion rate?
USE largedataset;

-- 1. How many total records are in the dataset?  

SELECT 
	COUNT(*) AS total_records
FROM h_insurance;

-- 18. What percentage of total leads responded positively? (subquery or calculation)

SELECT
    CASE
        WHEN Response = 1 THEN 'Positive Response'
        ELSE 'Negative Response'
    END AS Responses,
    COUNT(*) AS Total,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM h_insurance), 2) AS Percentage
FROM h_insurance
GROUP BY Responses;

-- Demographics, accommodation, existing policy holders

-- 3. How many customers own their accommodation vs. rent it?

SELECT
	Accomodation_Type,
    COUNT(*) AS total
FROM h_insurance
GROUP BY Accomodation_Type;

-- 4. How many customers have a Joint insurance type vs. Individual?

SELECT
	Reco_Insurance_Type,
    COUNT(*) AS total
FROM h_insurance 
GROUP BY Reco_Insurance_Type;

-- 5. How many customers have a spouse (Is_Spouse = Yes)?

SELECT 
	Is_Spouse AS have_a_spouse,
	COUNT(*) AS total
FROM h_insurance
GROUP BY Is_Spouse;

-- 7. How many leads are from customers aged 60 and above (Upper_Age)?

SELECT 
	COUNT(*) AS leads_from_cus_above60
FROM h_insurance
WHERE Response=1 AND Upper_Age>=60;

-- 17. Classify customers into age groups (18–30, 31–45, 46–60, 60+) based on Upper_Age. How many leads fall in each group? (CASE WHEN)

SELECT
	CASE 
		WHEN Upper_Age BETWEEN 18 AND 30 THEN '18-30'
        WHEN Upper_Age BETWEEN 31 AND 45 THEN '31-45'
        WHEN Upper_Age BETWEEN 46 AND 60 THEN '46-60'
        ELSE '60+'
	END AS `Age Group`,
    SUM(Response) AS Leads
FROM h_insurance
GROUP BY `Age Group`
ORDER BY Leads DESC;

-- 20. Among customers with an existing policy (Holding_Policy_Type is not null), what is the response rate compared to those without?

SELECT 
	CASE 
		WHEN Holding_Policy_Type IS NOT NULL THEN 'Has Existing Policy'
        Else 'No Existing Policy'
	END AS `Existing Policy`,
	COUNT(*) AS `Total Customers`,
    SUM(Response) AS `Total Leads`,
    ROUND(SUM(Response) * 100.0 / COUNT(*), 2) AS `Response Rate %`
FROM h_insurance
GROUP BY `Existing Policy`
ORDER BY `Response Rate %` DESC;

-- What drives conversion?
-- Policy category, premium levels, city, age

-- 6. Which city code has the highest number of leads? (GROUP BY + ORDER BY + LIMIT)

SELECT
	City_Code,
	COUNT(*) AS total_leads
FROM h_insurance
WHERE Response=1
GROUP BY City_Code
ORDER BY total_leads DESC
LIMIT 1;

-- 12. What is the average recommended premium across all leads?

SELECT
	ROUND(AVG(Reco_Policy_Premium),2) AS `Average recommended premium across all leads`
FROM h_insurance
WHERE Response=1;
    
-- 13. What is the average premium for customers who responded (=1) vs. those who didn't (=0)? — This is a key business insight!

SELECT
	Response,
	ROUND(AVG(Reco_Policy_Premium), 2) AS `Average Recommended Premium`
FROM h_insurance
GROUP BY Response;
    
-- 14. Which accommodation type (Owned/Rented) has a higher average policy premium?

SELECT 
	Accomodation_Type,
    ROUND(AVG(Reco_Policy_Premium), 2) AS `Average Recommended Premium`
FROM h_insurance
GROUP BY Accomodation_Type
ORDER BY `Average Recommended Premium` DESC;

-- 16. How many leads fall under each Reco_Policy_Cat category?

SELECT 
	Reco_Policy_Cat,
    SUM(Response) AS `Total leads`
FROM h_insurance
GROUP BY Reco_Policy_Cat
ORDER BY `Total leads` DESC;

-- 19. Which city has the highest conversion rate (Response = 1)? (GROUP BY city, calculated rate)

SELECT
	City_Code AS `City Code`,
    COUNT(*) AS `Total Customers`,
    SUM(Response) AS `Total Leads`,
    ROUND(SUM(Response) * 100.0 / COUNT(*), 2) AS `Conversion Rate`
FROM h_insurance
GROUP BY City_Code
ORDER BY `Conversion Rate` DESC
LIMIT 1;

-- Data quality
-- What's missing and does it matter?

-- 8. How many records have missing Health Indicator data? (IS NULL) 

SELECT 
	COUNT(*) AS `No. of Missing Health Indicator Records`
FROM h_insurance
WHERE `Health Indicator` IS NULL;

-- 9. How many records have missing Holding_Policy_Duration?

SELECT 
	COUNT(*)
FROM h_insurance
WHERE Holding_Policy_Duration IS NULL;

-- 10. How many customers are both a spouse AND responded positively?

SELECT
	COUNT(*) AS `Customers with spouse and positive response`
FROM h_insurance
WHERE Is_Spouse='Yes' AND Response=1;

-- 11. List all leads where the recommended premium is above ₹25,000.

SELECT 
	Id,
    Reco_Policy_Premium AS `Recommended Premium`
FROM h_insurance
WHERE Reco_Policy_Premium>25000
ORDER BY `Recommended Premium` DESC;



-- 15. What is the average age gap (Upper_Age - Lower_Age) per insurance type (Individual/Joint)?
# This question is unnecesary for individual account but as per the question both are mentioned.

SELECT
	Reco_Insurance_Type AS `Insurance Type`,
	AVG(Upper_Age) AS `Average Upper Age`,
    AVG(Lower_Age) AS `Average Lower Age`,
    AVG(Upper_Age)-AVG(Lower_Age) AS `Average age gap`
FROM h_insurance
GROUP BY Reco_Insurance_Type;


