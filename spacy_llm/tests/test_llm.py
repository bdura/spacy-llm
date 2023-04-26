from typing import Any, Dict

import minichain
import pytest
import spacy
from ..pipeline import LLMWrapper


@pytest.fixture
def nlp() -> spacy.Language:
    nlp = spacy.blank("en")
    nlp.add_pipe("llm")
    return nlp


def test_llm_init(nlp):
    """Test pipeline intialization."""
    assert ["llm"] == nlp.pipe_names


def test_llm_pipe(nlp):
    """Test call .pipe()."""
    docs = list(nlp.pipe(texts=["This is a test", "This is another test"]))
    assert len(docs) == 2


def test_llm_serialize_bytes():
    llm = LLMWrapper(
        template=None,  # type: ignore
        api=lambda: minichain.OpenAI(),
        prompt=None,  # type: ignore
        parse=None,  # type: ignore
    )
    llm.from_bytes(llm.to_bytes())


def test_llm_serialize_disk():
    llm = LLMWrapper(
        template=None,  # type: ignore
        api=lambda: minichain.OpenAI(),
        prompt=None,  # type: ignore
        parse=None,  # type: ignore
    )

    with spacy.util.make_tempdir() as tmp_dir:
        llm.to_disk(tmp_dir / "llm")
        llm.from_disk(tmp_dir / "llm")


@pytest.mark.parametrize(
    "config",
    (
        {
            "api": "spacy.api.MiniChain.v1",
            "backend": "OpenAI",
            "config": {},
            "prompt": "spacy.prompt.MiniChainSimple.v1",
        },
        {
            "api": "spacy.api.LangChain.v1",
            "backend": "openai",
            "config": {"temperature": 0.3},
            "prompt": "spacy.prompt.LangChainSimple.v1",
        },
    ),
)
def test_integrations(config: Dict[str, Any]):
    """Test simple runs with all supported integrations."""
    nlp = spacy.blank("en")
    nlp.add_pipe(
        "llm",
        config={
            "api": {
                "@llm": config["api"],
                "backend": config["backend"],
                "config": config["config"],
            },
            "prompt": {"@llm": config["prompt"]},
        },
    )