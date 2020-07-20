import familiar
from scipy.stats import ttest_1samp
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency

# first we want to show that the most basic package, the Vein Pack, has a significant impact on the subscribers' lifespan
# lifespans of Vein Pack users are returned by the function lifespans(package='vein'), which is part of the familiar module 
vein_pack_lifespans = familiar.lifespans(package='vein')

# find out if the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 71 years
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(format(vein_pack_test.pvalue, '0.10f'))
# p < .01

average_age_vein_pack = sum(vein_pack_lifespans) / len(vein_pack_lifespans)
print(average_age_vein_pack)
# average lifespan of Vein Pack subscribers is 76.2

if vein_pack_test.pvalue < 0.05:
  print('The Vein Pack is Proven To Make You Live Longer!')
else:
  print('The Vein Pack is Probably Good For You Somehow')
# life expectancy for Vein Pack subscribers appears to be significantly higher than the average life expectancy of 71 years

# next we want to compare lifespan data between the different packages. The next step up from the Vein Pack is the Artery Pack. Get the lifespans of Artery Pack subscribers using the same method
artery_pack_lifespans = familiar.lifespans(package='artery')

# find out if Artery Pack subscribers experience a significant improvement in lifespan compared to the Vein Pack subscribers
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print(format(package_comparison_results.pvalue, '0.10f'))
# p = .056

if package_comparison_results.pvalue < 0.05:
  print('the Artery Package guarantees even stronger results!')
else:
  print('the Artery Package is also a great product')
# there appears to be no significant difference in lifespan between Vein Pack subscribers and Artery Pack subscribers

# to do an extra analysis on potential benefits a survey was being sent out to collect the iron counts for Vein Pack and Artery Pack subscribers. This data is formatted into a contingency table and divided in low, normal and high iron counts
iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)

# find out if there is a significant difference in iron counts from what was reported between the two groups, safe the p-value in a variable called iron_pvalue
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table) 
print(format(iron_pvalue, '0.10f'))
# p < .01

if iron_pvalue < 0.05:
  print('The Artery Package is Proven to Make you Healthier!')
else:
  print("While we can't say the Artery Package Will Help You, I Bet it's Nice!")
# there appears to be a significant difference in iron counts between Vein Pack subscribers and Artery Pack subscribers, the Artery package seems to make you even healthier than the Vein Package
 
