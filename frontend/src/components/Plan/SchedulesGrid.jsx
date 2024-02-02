import { useSelector } from "react-redux";
import useAutoFetch from "../../hooks/useAutoFetch.js";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner.jsx";
import { GridContainer } from "./SchedulesGrid.style.js";
import SchedulesPerMonth from "./SchedulesPerMonth.jsx";
import Weekdays from "./Weekdays.jsx";

export default function SchedulesGrid({ plan_id }) {
  const isLoggedIn = useSelector((store) => store.loggedInUser.accessToken);
  const endpointToFetch = isLoggedIn
    ? `schedules`
    : `schedules_without_logged_in`;
  const { data: allSchedules } = useAutoFetch(
    "get",
    `plans/${plan_id}/${endpointToFetch}`
  );

  if (!allSchedules) return <LoadingSpinner />;

  const schedulesByMonth = allSchedules.reduce((acc, schedule) => {
    const date = new Date(schedule.date);
    const key = date.getMonth();
    if (!acc[key]) acc[key] = [];
    acc[key].push(schedule);
    return acc;
  }, {});

  return (
    <>
      <GridContainer>
        <Weekdays />
      </GridContainer>

      {Object.entries(schedulesByMonth).map((item) => (
        <SchedulesPerMonth key={item[0]} schedules={item[1]} />
      ))}
    </>
  );
}
