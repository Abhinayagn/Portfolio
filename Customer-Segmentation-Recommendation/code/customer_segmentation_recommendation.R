
#----------------------------------
# LOADING REQUIRED LIBRARIES
#----------------------------------

library(dplyr)
library(tidyr)
library(ggplot2)
library(cluster)
library(arules)
library(arulesViz)
library(readxl)
#----------------------------------
# LOADING DATASETS
#----------------------------------

customer_data <- read.csv("customer_data.csv")
customer_purchase_history <- read.csv("customer_purchase_history_final.csv")

#---------------------------------
# DATA EXPLORATION
#---------------------------------

summary(customer_data)
summary(customer_purchase_history)
str(customer_data)
str(customer_purchase_history)

#---------------------------------
# DATA CLEANING
#---------------------------------

# Checking for missing values
sapply(customer_data, function(x) sum(is.na(x)))
sapply(customer_purchase_history, function(x) sum(is.na(x)))

#Replace empty values with the mean values of the column in a dataset if required

customer_data=customer_data[2:5]
customer_data <- customer_data %>%
  mutate(across(where(is.character), as.factor)) %>%
  mutate(across(where(is.numeric), ~ replace_na(., mean(., na.rm = TRUE))))

# Visualizing Data


hist(customer_data[, 1],main='Age Distribution',xlab='Age') # Histogram for age distribution
hist(customer_data[, 2],main='Salary Distribution',xlab='Salary') # Histogram for salary distribution
hist(customer_data[, 3],main='Spending Score Distribution',xlab='Spending Score') # Histogram for spending score distribution
hist(customer_data[, 4],main='Time as Customer Distribution',xlab='Time as Customer')
#-------------------------------
#CUSTOMER SEGMENTATION
#-------------------------------

#K-MEANS classification Model

# Using the elbow method to find the optimal number of clusters

# Used for selecting the most appropriate K value

set.seed(314)  # Set random seed for reproducibility
wcss = vector()
for (i in 1:15) wcss[i] = sum(kmeans(customer_data, i)$withinss)
plot(x = 1:15,
     y = wcss,
     type = 'b',
     main = paste('The Elbow Method'),
     xlab = 'Number of clusters',
     ylab = 'WCSS')


# Fitting K-Means to the model

set.seed(214) # Set random seed again for reproducibility
kmeans = kmeans(x = customer_data,
                centers = 4,
                iter.max = 300,
                nstart = 10)      # Perform K-Means with 3 clusters
n_clusters <- length(unique(kmeans$cluster))
kmeans

#------------------------------
# VISUALIZING THE CLUSTERS
#------------------------------

# Having columns 'Salary' and 'Spending Score' in customer data

plot(customer_data$salary, customer_data$`spendingScore`, 
     col = kmeans$cluster, 
     pch = 16, 
     xlab = "Salary", ylab = "Spending Score", main = "Clusters of Customers")

legend("topright", legend = paste("Cluster", 1:n_clusters), col = 1:n_clusters, pch = 16)

# 3-Dimensional Visualization of cluster

library(scatterplot3d)
scatterplot3d(customer_data$salary,customer_data$spending_score,customer_data$time_as_customer, 
              color = kmeans$cluster, pch = 16, main = "Clusters of Customers")
legend("topright", legend = paste("Cluster", 1:n_clusters), col = 1:n_clusters, pch = 16)

#--------------------------------
# RECOMENDATION ENGINE
#--------------------------------

#Association rule mining


# Load the dataset and Convert purchase_history into a transaction format for association rule mining 

data <- read.transactions(file = "customer_purchase_history_final.csv", sep = ",", rm.duplicates = TRUE)


#Finding the  Top 10 most purchased products
itemFrequencyPlot(data, topN=10, main="Top 10 Most Purchased Products",xlab="Products",ylab="Frequency")


# Using of Eclat Algorithm to find most purchased products


# Eclat Algorithm (Equivalance Class Transformation)

library(arules)
rules_eclat <- eclat(data, parameter = list(support = 0.003, minlen = 2))
summary(rules_eclat)
inspect(sort(rules_eclat, by = 'support')[1:20])



