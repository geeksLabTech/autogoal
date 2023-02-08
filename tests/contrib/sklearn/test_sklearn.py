import pytest

from autogoal.contrib import find_classes
from autogoal.grammar import generate_cfg, Sampler
from autogoal.exceptions import InterfaceIncompatibleError

from autogoal.contrib import sklearn
from autogoal.contrib.sklearn._manual import CountVectorizerNoTokenize


classes = find_classes(modules=[sklearn], exclude="CountVectorizerNoTokenize")


@pytest.mark.contrib
@pytest.mark.parametrize("clss", classes)
def test_create_grammar_for_generated_class(clss):
    try:
        generate_cfg(clss, registry=classes)
    except InterfaceIncompatibleError:
        pass


@pytest.mark.slow
@pytest.mark.contrib
@pytest.mark.parametrize("clss", classes)
def test_sample_generated_class(clss):
    grammar = generate_cfg(clss, registry=classes)
    sampler = Sampler(random_state=0)

    for _ in range(1000):
        grammar.sample(sampler=sampler)
