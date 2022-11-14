select *
from tblproducts p
join schedule s on p.pk_tblproducts=s.idx 
join scheduleprojecttypes spt on s.sptidx=spt.sptidx
where spt.stidx=1  