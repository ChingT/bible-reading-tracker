import { useEffect, useState } from "react";
import useApiRequest from "../../hooks/useApiRequest.js";

function ScheduleComponent({ initSchedule, books }) {
  const { sendRequest, data } = useApiRequest();
  const [schedule, setSchedule] = useState(initSchedule);

  useEffect(() => {
    if (data) setSchedule(data);
  }, [data]);

  const handleToggleSelection = (schedule_id) => {
    sendRequest("patch", `plans/finished_schedule/${schedule_id}`);
  };

  const find_book_name = (book_id) => {
    const book = books.find((book) => book.id === book_id);
    return book.short_name_de;
  };

  const PassageComponent = (passage) => (
    <div key={passage.id}>
      <p>
        {find_book_name(passage.book_id)} {passage.verses}
      </p>
    </div>
  );
  return (
    <div>
      <input
        type="checkbox"
        checked={schedule.is_finished_by_logged_in_user}
        onChange={() => handleToggleSelection(schedule.id)}
      />
      <div>{schedule.date}</div>
      {schedule.passages.map(PassageComponent)}
    </div>
  );
}

export default ScheduleComponent;