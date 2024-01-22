import { ErrorMessage, InputFieldContainer } from "../Layout/Layout.style.js";

const InputField = ({
  userData,
  handleInput,
  type,
  placeholder,
  error,
  icon,
  id,
  label,
  span,
}) => {
  return (
    <InputFieldContainer $span={span}>
      {label && <label htmlFor={id}>{label}</label>}
      <div className={"input-wrapper"}>
        {icon && <img src={icon}></img>}
        <input
          placeholder={placeholder}
          type={type}
          value={userData[id] === undefined ? "" : userData[id]}
          onChange={handleInput}
          id={id}
        />
      </div>
      {error && error[id] && <ErrorMessage>{error[id]}</ErrorMessage>}
    </InputFieldContainer>
  );
};

export default InputField;
