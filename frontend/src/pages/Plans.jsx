import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import LoadingSpinner from "../components/LoadingSpinner/LoadingSpinner.jsx";
import SchedulesGrid from "../components/Schedule/SchedulesGrid.jsx";
import useAutoFetch from "../hooks/useAutoFetch.js";
import { loadBooks } from "../store/slices/loadedBooks.js";

function Plans() {
  const { data } = useAutoFetch("get", "plans", null, true);
  const { data: books } = useAutoFetch("get", "books");
  const [plans, setPlans] = useState(null);
  const dispatch = useDispatch();

  useEffect(() => {
    if (data) setPlans(data);
  }, [data]);

  useEffect(() => {
    if (books) dispatch(loadBooks(books));
  }, [books, dispatch]);

  if (!plans) return <LoadingSpinner />;

  const PlanComponent = (plan) => (
    <div key={plan.id}>
      <h2>{plan.title}</h2>
      <p>{plan.description}</p>
      <SchedulesGrid plan_id={plan.id} />
    </div>
  );

  return <>{plans.map(PlanComponent)}</>;
}

export default Plans;
