# Project-1

![SchoolHome](SchoolandHome.png)

# <p align="center"> Housing and Schooling </p>
  <p align="center"> Where to go for the perfect house for your family and the perfect school for your children. </p>

## Premise
We are working for a real estate company in the Dallas-Fort Worth Metroplex that wishes to specialise in sellings homes to families coming into the area. 

We have created  a Dashboard where parents/potential house buyers can easily click through the public school districts in the four main DFW Counties to see what is the best bang for their buck they can get school district wise. 

## Data

We cleaned up the data from multiple sources, the previously mentioned TEA and Appraisal Districts for the counties. We combined the data into a single .csv file.

**Data Included**
| Years  | Type of Data  |
| ------------- | ------------- |
| N/A |  County Name  |
| N/A | School District Name  |
| 2019 | Median Income |
|2016-20 |Total Property Values per ISD |
|2016-20 |Median Property Values per ISD | 
|2016-20 |Taxes Due per ISD |
|2016-20 |Annual Taxes Due |
|2018/19 | District Academic Ratings |

**Potential Data Issues** 

* School District Ratings: Only two years of Data due to a change in Ratings to A-F from a pass-fail in previous years and a lack of data due to the strange 2020 Covid school year. 
   

Finalized Data: [School District Rankings & Property Tax](dfw_real_estate_isd.csv)

## Process

* TEA spreadsheets provide comptroller tax information, including property tax rates by district for the specified tax years. These files that were downloaded from the site needed to be shortented. A district's property tax rate consists of a maintenance and operations (M&O) tax rate and, an interest and sinking (I&S) tax rate. The M&O tax rate provides funds for maintenance and operations. 
* The I&S tax rate provides funds for payments on the debt that finances a district's facilities. The calculation of state funding for school districts is tied to tax effort; thus, tax rates provide an essential component in the state's school finance formulas. With these detail informations, one master .csv file is created.
* The data had school Rating in Character. The character representation were transformed into numeric representation with 4 scale.
* The API from Texas Education Agency Public Open Data Site was used for getting the  current school information. The API  covers school educational information along with schools' locations, schools' contact information, such as phone numbers, fax numbers, emails,  and school scores.
* The data collected from both sources were cleaned. Some of the null value were fill with value accordingly

## Analysis

## Charts

![GraphTwo](Graphs/Rating_By_Income.png)

![GraphThree](Graphs/Rating_By_Value.png)

![GraphFour](Graphs/Rating_By_TaxDue.png)

![GraphFive](Graphs/Rating_By_TaxRate.png)

## GIF of Dashboard
![GifOne](Bar_Analysis_Tab.gif)
![GifTwo](Sunburst_Tab.gif)
![GifThree](District_Rating_Tab.gif)

## Project Worked On By: 
* [Jimmy Brown](https://github.com/jbrown2155) Primary Data Cleaner & Gatherer/Reviewed code.
* [Syeda Hasan](https://github.com/rimpi1612) Primary Coder
* [David Ready](https://github.com/CrusadingGroundhog) Primary work for Read.Me / Reviewed code.
* [Samson Bui](https://github.com/SamsonBui)
