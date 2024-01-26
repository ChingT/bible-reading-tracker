import { CardTitle } from "./SchedulesGrid.style";

function Weekdays() {
  const weekdays = [
    "Tag des Herrn",
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
  ];

  return weekdays.map((weekday) => (
    <CardTitle key={weekday}>{weekday}</CardTitle>
  ));
}

export default Weekdays;
