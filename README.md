NUS HYP Tracker
===============
For tracking newly-listed NUS HYP, FYP and UROP Projects that peskily and silently pop up in the middle of nowhere without any notice.

I was checking the HYP / FYP / UROP List, for projects that would interest me.

The problem was that it kept updating itself without any indication of the changes made. It was very tedious to check the list for new projects that were added as the faculty for some reason, chose not to show them separately - They kept adding new projects without telling us, right in the middle of existing projects... which meant that I had to manually keep track of all the changes. So I wrote this code to save me some time in checking the list.

It's the minimum code required to be useful at the moment because it was meant to be a quickfix, written to save me some time.

Also note that it was written with the SoC HYP listing platform in mind. I'm not sure what the other HYP platforms from the other faculties look like, so there is no guarantee that it will work with them.


How to Use
---------------
The instructions will appear when you run the Python script.	
1. Save the list you read previously under the file name FYPOldList.txt		
2. Save the current list under the file name FYPNewList.txt		
3. The new results will appear in FYP_allNew.txt	


Future Improvements
---------------
There's a way for you to contribute if you want to.		
1. First improvement. Import requests, use it for auth and to get the actual webpage.	
2. Next improvement. Parse the html to get the list.	
3. Save list in txt file with timestamp in filename instead of static filename.		
4. Dynamic table list creation, based on the parsed data from the retrieved html, so that the code can work with any HYP Listing platform from any faculty.

Ok have fun.