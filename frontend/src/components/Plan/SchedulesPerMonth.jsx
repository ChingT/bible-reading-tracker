import ScheduleCard from "./ScheduleCard.jsx";
import { GridContainer } from "./SchedulesGrid.style.js";

export default function SchedulesPerMonth({ schedules, books }) {
  const firstDay = new Date(schedules[0].date);
  const month = new Intl.DateTimeFormat("de-DE", { month: "long" }).format(
    firstDay
  );
  const emptyCards = [...Array(firstDay.getDay())].map((_, i) => (
    <div key={i}></div>
  ));
  return (
    <div key={month}>
      <h2>{month}</h2>
      <GridContainer>
        {emptyCards}
        {schedules.map((schedule) => (
          <ScheduleCard
            key={schedule.id}
            initSchedule={schedule}
            books={books}
          />
        ))}
      </GridContainer>
    </div>
  );
}
