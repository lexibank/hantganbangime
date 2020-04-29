
def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


# "we further extracted a selection of 22 languages and 300 concepts..."
def test_languages(cldf_dataset, cldf_logger):
    assert len(list(cldf_dataset['LanguageTable'])) == 22


def test_parameters(cldf_dataset, cldf_logger):
    assert len(list(cldf_dataset['ParameterTable'])) == 300


def test_sources(cldf_dataset, cldf_logger):
    assert len(cldf_dataset.sources) == 93


def test_forms(cldf_dataset, cldf_logger):
    assert len(list(cldf_dataset['FormTable'])) == 6181
    # check one at random
    assert len([
        f for f in cldf_dataset['FormTable'] if f['Form'] == 'ɡwìì'
    ]) == 1
