import { CardTitle } from "./SchedulesGrid.style";

export default function Weekdays() {
  const numberOfDays = 7;
  const weekdaysMap = {};
  [...Array(numberOfDays)].forEach((_, i) => {
    const date = new Date(2024, 0, i + 1);
    weekdaysMap[date.getDay()] = date.toLocaleDateString("de-DE", {
      weekday: "long",
    });
  });

  return [...Array(numberOfDays)].map((_, i) => (
    <CardTitle key={weekdaysMap[i]}>{weekdaysMap[i]}</CardTitle>
  ));
}
