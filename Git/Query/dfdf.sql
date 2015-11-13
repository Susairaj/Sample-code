SELECT * 
  FROM public.calendar 
 WHERE calendarid NOT IN (SELECT calendarbookingid 
                    FROM public.calendarbooking) 
ORDER BY calendarid desc
