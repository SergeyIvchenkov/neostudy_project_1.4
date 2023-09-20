
CREATE OR REPLACE FUNCTION dm.db_cr_date(input_date date)
 RETURNS TABLE(oper_date date, max_credit_amount numeric(19,4), min_credit_amount numeric(19,4), max_debet_amount numeric(19,4), min_debet_amount numeric(19,4))
 LANGUAGE plpgsql
AS $function$
begin
	return query
		select pf.oper_date, max(pf.credit_amount)::numeric(19,4), min(pf.credit_amount)::numeric(19,4), max(pf.debet_amount)::numeric(19,4), min(pf.debet_amount)::numeric(19,4)
		from ds.ft_posting_f pf
		where pf.oper_date = input_date
		group by 1;
end;
$function$
;

select * from dm.db_cr_date('2018-01-10')