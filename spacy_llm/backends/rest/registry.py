from typing import Callable, Iterable, Dict, Any

import spacy
from spacy.util import SimpleFrozenDict
from .backend import Backend


@spacy.registry.llm_backends("spacy.REST.v1")
def backend_rest(
    api: str,
    config: Dict[Any, Any] = SimpleFrozenDict(),
    strict: bool = True,
) -> Callable[[Iterable[str]], Iterable[str]]:
    """Returns Callable using minimal REST backend to prompt specified API.
    api (str): Name of any API. Currently supported: "OpenAI".
    config (Dict[Any, Any]): LLM config arguments passed on to the initialization of the Backend instance.
    strict (bool): If True, ValueError is raised if the LLM API returns a malformed response (i. e. any kind of JSON
        or other response object that does not conform to the expectation of how a well-formed response object from
        this API should look like). If False, the API error responses are returned by __call__(), but no error will
        be raised.
    RETURNS (Callable[[Iterable[str]], Iterable[str]]]): Callable using the querying the specified API using a
        Backend instance.
    """

    backend = Backend(api=api, config=config, strict=strict)

    def _query(prompts: Iterable[str]) -> Iterable[str]:
        return backend(prompts)

    return _query