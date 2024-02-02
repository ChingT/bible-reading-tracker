import Tooltip from "@mui/material/Tooltip";
import { useEffect, useState } from "react";
import { useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import useApiRequest from "../../hooks/useApiRequest.js";
import Checkbox from "../../styles/checkbox.jsx";
import { CardContainer } from "./Schedule.style.js";

export default function ScheduleCard({ initSchedule }) {
  const isLoggedIn = useSelector((store) => store.loggedInUser.accessToken);
  const { sendRequest, data } = useApiRequest();
  const [schedule, setSchedule] = useState(initSchedule);
  const navigate = useNavigate();

  useEffect(() => {
    if (data) setSchedule(data);
  }, [data]);

  const handleToggleSelection = (e) => {
    e.preventDefault();
    if (isLoggedIn) {
      sendRequest("patch", `plans/finished_schedule/${schedule.id}`);
    } else {
      navigate("/signin");
    }
  };

  return (
    <CardContainer onClick={handleToggleSelection}>
      <div>
        <Checkbox checked={schedule.is_finished_by_logged_in_user} />
        <CardDate date={schedule.date} />
      </div>

      {schedule.passages.map((passage) => (
        <Passage key={passage.id} passage={passage} />
      ))}
    </CardContainer>
  );
}

const dateStyle = { month: "short", day: "numeric" };

function CardDate({ date }) {
  const day = new Intl.DateTimeFormat("de-DE", dateStyle).format(
    new Date(date)
  );
  return <p>{day}</p>;
}

function Passage({ passage }) {
  const books = useSelector((store) => store.loadedBooks.books);
  const book = books.find((book) => book.id === passage.book_id);
  const fullName = `${book.full_name_de} ${passage.verses}`;
  const shortName = `${book.short_name_de} ${passage.verses}`;

  return (
    <Tooltip title={fullName}>
      <p>{shortName}</p>
    </Tooltip>
  );
}
