import ScheduleCard from "./ScheduleCard.jsx";
import { GridContainer } from "./SchedulesGrid.style.js";

export default function SchedulesPerMonth({ schedules }) {
  const firstDay = new Date(schedules[0].date);
  const month = new Intl.DateTimeFormat("de-DE", {
    month: "long",
    year: "numeric",
  }).format(firstDay);
  const emptyCards = [...Array(firstDay.getDay())].map((_, i) => (
    <div key={i}></div>
  ));
  return (
    <div>
      <h2>{month}</h2>
      <GridContainer>
        {emptyCards}
        {schedules.map((schedule) => (
          <ScheduleCard key={schedule.id} initSchedule={schedule} />
        ))}
      </GridContainer>
    </div>
  );
}
