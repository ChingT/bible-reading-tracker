import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import useAutoFetch from "../../hooks/useAutoFetch.js";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner.jsx";
import ProgressBar from "../ProgressBar/ProgressBar.jsx";
import { GridContainer } from "./Schedule.style.js";
import SchedulesPerMonth from "./SchedulesPerMonth.jsx";
import Weekdays from "./Weekdays.jsx";

export default function SchedulesGrid({ plan_id }) {
  const [numFinishedSchedules, setNumFinishedSchedules] = useState(0);
  const isLoggedIn = useSelector((store) => store.loggedInUser.accessToken);
  const endpointToFetch = isLoggedIn
    ? `schedules`
    : `schedules_without_logged_in`;
  const { data: allSchedules } = useAutoFetch(
    "get",
    `plans/${plan_id}/${endpointToFetch}`
  );

  useEffect(() => {
    if (allSchedules) {
      setNumFinishedSchedules(
        allSchedules.filter(
          (schedule) => schedule.is_finished_by_logged_in_user
        ).length
      );
    }
  }, [allSchedules]);

  if (!allSchedules) return <LoadingSpinner />;

  const schedulesByMonth = allSchedules.reduce((acc, schedule) => {
    const date = new Date(schedule.date);
    const key = `${date.getFullYear()}-${date.getMonth()}`;
    if (!acc[key]) acc[key] = [];
    acc[key].push(schedule);
    return acc;
  }, {});

  return (
    <>
      <ProgressBar
        numFinishedSchedules={numFinishedSchedules}
        numSchedules={allSchedules.length}
      />

      <GridContainer>
        <Weekdays />
      </GridContainer>

      {Object.entries(schedulesByMonth).map((item) => (
        <SchedulesPerMonth
          key={item[0]}
          schedules={item[1]}
          setNumFinishedSchedules={setNumFinishedSchedules}
        />
      ))}
    </>
  );
}
