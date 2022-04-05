
# Jr Data Scientist - Evaluation -1 


## Part 1
1. Write a regex to extract all the numbers with orange color background from the below text in italics.
## Answer
Problem1.py (In Repository)

2. Problem statement - There are times when a user writes Good, Nice App or any other positive text, in the review and gives 1-star rating. Your goal is to identify the reviews where the semantics of review text does not match rating. 
## Answer

## Mismatch prediction based on customer reviews and ratings

 https://2689-117-196-18-7.ngrok.io 

Customers' reviews and ratings are helping businesses improve their services and products these days, but some reviews are mismatched to their star rating, affecting the overall rating of the product or service. For example, there are times whenever a user writes Good, Nice, or any other positive text in a review and gives a 1-star rating.

The goal of this research is to do sentiment analysis and develop a model that can predict positive and negative messages. I also want to create an app that can be used to track down customers who leave nice reviews but have a low rating, and then create a developer response for them. There is a discrepancy between the star rating and the reviews.

## Sentiment analysis
Sentiment analysis is contextual mining of text which identifies and extracts subjective information in source material, and helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations.
## Vectorization
Word Embeddings or Word vectorization is a methodology in NLP to map words or phrases from vocabulary to a corresponding vector of real numbers which used to find word predictions, word similarities/semantics. The process of converting words into numbers are called Vectorization.
## Modelling
I utilized logistic regression for modeling, and it gave me a 79 percent accuracy.
 ## Flask App
 I saved the final tuned logistic regression model and deployed it using Flask web app. Flask is a micro web framework written in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

Demo https://drive.google.com/file/d/16d4TA3GNxkQz37CbQFfT-LKAElCpMiwE/view?usp=sharing

## Part 2 
More Bonus points (You can write answers to these in ReadMe)

1. difficult problems


-- The first major issue I had was with my laptop display, which kept me stuck for few days until I was able to acquire a laptop from my brother in law. During that time I research about my project via mobile phone

In the basic sentiment analysis model, almost all classifications work excellently, but in the real world, performance deteriorates.

Another problem is finding a suitable pre-trained model.

I spent a lot of time on web hosting with Heroku, and I received a lot of errors, so I utilized ngrok because of the time constraint.

I spent a lot of time looking for a pretrained model for the grammar checking problem, and while I found one that worked, I couldn't find an appropriate data set for it.


2. Which of the following is a subspace of V?


## Subspaces
Suppose that 
V
 is a vector space and 
W
 is a subset of 
V
, 
W
⊆
V
. Endow 
W
 with the same operations as 
V
. Then 
W
 is a subspace if and only if three conditions are met

 1. W is nonempty, 
W
≠
∅
.

2. If 
x
∈
W
 and 
y
∈
W
, then 
x
+
y
∈
W
.

3. If 
α
∈
C
 and 
x
∈
W
, then 
α
x
∈
W
.

## solution
- K=The set of pairs (a, a + 1) for all real a

-- (0,0) not in K , so K not a subspace of V

- K=The set of pairs (a, b) for all real a ≥ b

-- (0,0) in K 

-- (a1,b1) and (a2,b2) in K where a1>=b1 and a2>=b2
such that ((a1+a2),(b1+b2)) also in K , bcz a1+a2>b1+b2

-- (10,1) belongs K
consider C=-1
then, (-10,-1) not belongs to K bcz  -10 < -1
therfore K not a subspace of V

- K= The set of pairs (a, 2a) for all real a

-- (0,0) in K

-- (a1,2a1) , (b2,2b2) belongs to K then

((a1+b2),2(a1+b2)) is also belongs to K

-- C= any R
then C*(a,2a) also belongs to K
therefor K is Subspace of V

- K=The set of pairs (a, b) for all non-negative real a,b

-- (0,0) belongs to K
-- (a1,b1) , (a2,b2) belongs to K then
((a1+a2),(b1+b2)) also in K

-- Cosider C= -1
 (5,1) in K but (-5,-1) not in K

 therefor K not a Subspace of V