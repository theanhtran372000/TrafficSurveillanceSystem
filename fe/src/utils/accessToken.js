export function getAccessToken(instance) {
  return instance.defaults.headers.common["Authorization"];
}

export function setAccessToken(instance, token) {
  instance.defaults.headers.common["Authorization"] = token;
}

export function resetAccessToken(instance) {
  setAccessToken(instance, null);
}
