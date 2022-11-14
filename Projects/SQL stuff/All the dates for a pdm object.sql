DECLARE @cnt INT = 0;
DECLARE @searchTarget VARCHAR(50) = 'IFVUEN215';
DECLARE @searchidx INT;
DECLARE @temp VARCHAR(50);
set @searchidx = (select TOP (1) IDX from [RDDatabase].[dbo].[CatalogItems] where Product = @searchTarget)

WHILE @cnt < 171
BEGIN
	IF dbo.Schedule_GetActualDate(@searchidx, @cnt) IS NOT NULL
	BEGIN
		set @temp = (select TOP (1) DateName from [RDDatabase].[dbo].[ScheduleDateNames] where sdnIDX = @cnt)
		print(@temp)
		print(dbo.Schedule_GetActualDate(@searchidx, @cnt));
	END
	SET @cnt = @cnt + 1;
END;
  
GO
