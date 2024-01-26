import { useEffect, useState } from "react";
import useAutoFetch from "../../hooks/useAutoFetch.js";
import LoadingSpinner from "../LoadingSpinner/LoadingSpinner.jsx";
import SchedulesGrid from "./SchedulesGrid.jsx";

function Plans() {
  const { data } = useAutoFetch("get", "plans", null, true);
  const [plans, setPlans] = useState(null);

  useEffect(() => {
    if (data) setPlans(data);
  }, [data]);

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
