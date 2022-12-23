export function isOk(response) {
  return response.status >= 200 && response.status <= 299;
}
