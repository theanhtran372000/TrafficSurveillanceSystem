import C from "@/constants";

export function getAccessToken() {
  return localStorage.getItem(C.__token_key__);
}

export function setAccessToken(instance, token) {
  if (token) {
    localStorage.setItem(C.__token_key__, token);
    instance.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  }
}

export function resetAccessToken(instance) {
  localStorage.removeItem(C.__token_key__);
}
