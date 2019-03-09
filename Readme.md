# Russian Airport

Use the following line to delete repeat line from database.

```sql
DELETE FROM russian_airport WHERE id NOT IN (SELECT MAX(id) from russian_airport GROUP BY airport, wikipage);
```

