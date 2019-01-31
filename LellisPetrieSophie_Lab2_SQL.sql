select * 
from (select BillingState, InvoiceYear, Total_Quantity, Name, rank() over (partition by InvoiceYear order by Total_Quantity desc) as Artist_Rank 
from (select inv.BillingState,strftime( '%Y', inv.InvoiceDate) as InvoiceYear, sum(ini.Quantity) as Total_Quantity, art.Name 
from invoices as inv left join invoice_items as ini on inv.InvoiceId = ini.InvoiceId 
left join tracks as tr on ini.TrackId = tr.TrackId
left join albums as alb on tr.AlbumId = alb.AlbumId
left join artists as art on alb.ArtistId = art.ArtistId 
where inv.BillingState = 'CA' group by 2,4) qry1 ) qry2 where qry2.Artist_Rank <= 3;