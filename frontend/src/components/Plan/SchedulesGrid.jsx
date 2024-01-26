import { useSelector } from "react-redux";
import useAutoFetch from "../../hooks/useAutoFetch.js";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner.jsx";
import ScheduleCard from "./ScheduleCard.jsx";
import { GridContainer } from "./SchedulesGrid.style.js";
import Weekdays from "./Weekdays.jsx";

function SchedulesGrid({ plan_id }) {
  const isLoggedIn = useSelector((store) => store.loggedInUser.accessToken);
  const endpointToFetch = isLoggedIn
    ? `schedules`
    : `schedules_without_logged_in`;
  const { data: schedules } = useAutoFetch(
    "get",
    `plans/${plan_id}/${endpointToFetch}`
  );
  const { data: books } = useAutoFetch("get", "books");

  if (!schedules || !books) return <LoadingSpinner />;

  return (
    <>
      <h3>Daily Schedules</h3>
      <GridContainer>
        <Weekdays />
        {schedules.map((schedule) => (
          <ScheduleCard
            key={schedule.id}
            initSchedule={schedule}
            books={books}
          />
        ))}
      </GridContainer>
    </>
  );
}

export default SchedulesGrid;
