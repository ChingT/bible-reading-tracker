import { useSelector } from "react-redux";
import useAutoFetch from "../../hooks/useAutoFetch.js";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner.jsx";
import ScheduleComponent from "./Schedule.jsx";

function Schedules({ plan_id }) {
  const isLoggedIn = useSelector((store) => store.loggedInUser.accessToken);
  const endpointToFetch = isLoggedIn
    ? `schedules`
    : `schedules_without_logged_in`;
  const { data: schedules } = useAutoFetch(
    "get",
    `plans/${plan_id}/${endpointToFetch}?limit=10`
  );
  const { data: books } = useAutoFetch("get", "books");

  if (!schedules || !books) return <LoadingSpinner />;

  return (
    <>
      <h3>Daily Schedules</h3>
      {schedules.map((schedule) => (
        <ScheduleComponent
          key={schedule.id}
          initSchedule={schedule}
          books={books}
        />
      ))}
    </>
  );
}

export default Schedules;
