# gtfs_realtime_json
Standalone utiltiy to convert gtfs-realtime feeds into simple JSON.

## Usage

Download [gtfs_realtime_json](https://github.com/harrytruong/gtfs_realtime_json/blob/master/dist/gtfs_realtime_json?raw=true) standalone, or compile from source.

Usage: 
```
$ gtfs_realtime_json <feed_url>
```

Examples:
```bash
$ gtfs_realtime_json "http://api.bart.gov/gtfsrt/tripupdate.aspx"
{"header":{"gtfs_realtime_version":"1.0","timestamp":1424843250, ... }

$ gtfs_realtime_json "http://api.bart.gov/gtfsrt/tripupdate.aspx" > output.json
// save JSON to output.json file
```

Sample JSON Outputs: 
  - MTA Trip Update [json](samples/mta-trip-updates.json)
  - BART Trip Update [json](samples/bart-trip-updates.json)

## GTFS-realtime Feed Sources

If you have any updates to this list, please message me or submit a PR!

*Last Updated: 02-25-2015*

#### Working Feeds:
  - MTA ([link](http://datamine.mta.info/))
     - Trip Updates (1, 2, 3, 4, 5, 6, S lines): `http://datamine.mta.info/mta_esi.php?key=<key>&feed_id=1`
     - Trip Updates (L line): `http://datamine.mta.info/mta_esi.php?key=<key>&feed_id=2`
     - Trip Updates (Staten Island Railway): `http://datamine.mta.info/mta_esi.php?key=<key>&feed_id=11`
     - *Note: NYCT's custom gtfs-realtime extensions have been included.*
     - *Note: An API key is required for these feeds.*
  
  - ART ([link](http://www.arlingtontransit.com/pages/rider-tools/tools-for-developers/))
     - Trip Updates: `http://realtime.commuterpage.com/rtt/public/utility/gtfsrealtime.aspx/tripupdate`
  
  - MBTA ([link](http://realtime.mbta.com/Portal/))
     - Service Alerts: `http://developer.mbta.com/lib/GTRTFS/Alerts/Alerts.pb`
     - Trip Updates: `http://developer.mbta.com/lib/GTRTFS/Alerts/TripUpdates.pb`
     - Vehicle Positions: `http://developer.mbta.com/lib/GTRTFS/Alerts/VehiclePositions.pb`
  
  - BART ([link](http://www.bart.gov/schedules/developers/gtfs-realtime))
     - Service Alerts: `http://api.bart.gov/gtfsrt/alerts.aspx`
     - Trip Updates: `http://api.bart.gov/gtfsrt/tripupdate.aspx`


#### Feeds Not Yet Confirmed:
  - Trimet ([link](http://developer.trimet.org/GTFS.shtml))

#### Feeds Not Working:
  - TransLink ([link](https://gtfsrt.api.translink.com.au/))

## Compiling

`$ virtualenv .venv`(optional)

`$ pip install -r requirements.txt`

`$ ./pyinstaller.sh` (See **dist/gtfs_realtime_json**)
