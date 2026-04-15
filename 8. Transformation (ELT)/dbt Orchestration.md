# dbt (data build tool)

**[⇐ Data Engineering Fundamentals](./README.md)**

## **dbt** Orchestration

### dbt Jobs

#### Cron Job Schedules


**Format**: [Minute] [Hour(24hr)] [day] [month] [weekday]

<small>  Visit [crontab.guru](https://crontab.guru/) to generate the correct cron syntax.  </small>

`*` = every  
`*/2` = every 2 min/hr/day/month/weekday  
`L` = last



Examples of cron job schedules:

- `0 * * * *`: Every hour, at minute 0.  
- `*/5 * * * *`: Every 5 minutes. (Not available on Developer plans)  
- `5 4 * * *`: At exactly 4:05 AM UTC.  
- `30 */4 * * *`: At minute 30 past every 4th hour (such as 4:30 AM, 8:30 AM, 12:30 PM, and so on, all UTC).  
- `0 0 */2 * *`: At 12:00 AM (midnight) UTC every other day.  
- `0 0 * * 1`: At midnight UTC every Monday.  
- `0 0 L * *`: At 12:00 AM (midnight), on the last day of the month.  
- `0 0 L 1,2,3,4,5,6,8,9,10,11,12 *`: At 12:00 AM, on the last day of the month, only in January, February, March, April, May, June, August, September, October, November, and December.  
- `0 0 L 7 *`: At 12:00 AM, on the last day of the month, only in July.  
- `0 0 L * FRI,SAT`: At 12:00 AM, on the last day of the month, and on Friday and Saturday.  
- `0 12 L * *`: At 12:00 PM (afternoon), on the last day of the month.  
- `0 7 L * 5`: At 07:00 AM, on the last day of the month, and on Friday.  
- `30 14 L * *`: At 02:30 PM, on the last day of the month.  
- `0 4 * * MON#1`: At 4:00 AM on the first Monday of every month.  