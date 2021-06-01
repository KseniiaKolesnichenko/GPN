import React, { useState, useCallback } from 'react'
import { Form, InputGroup, Button } from 'react-bootstrap'
import { Typeahead } from 'react-bootstrap-typeahead'

import 'react-bootstrap-typeahead/css/Typeahead.css'

import { TAGS } from '../../constants'

export const Search = () => {
    const [selected, setSelected] = useState([])

    const onSearchChange = useCallback((input) => setSelected(input), [])
    const onSearchButtonClick = useCallback(() => setSelected([]), [])

    return (
        <Form.Group>
            <InputGroup>
                <InputGroup.Prepend>
                    <InputGroup.Text>
                        Topics name
                    </InputGroup.Text>
                </InputGroup.Prepend>
                <Typeahead
                    id="tag-search"
                    labelKey="name"
                    multiple
                    clearButton
                    onChange={onSearchChange}
                    options={TAGS}
                    placeholder="Start typing tag..."
                    selected={selected}
                />
                <InputGroup.Append>
                    <Button variant="outline-success" onClick={onSearchButtonClick}>
                        Search
                    </Button>
                </InputGroup.Append>
            </InputGroup>
        </Form.Group>
    )
}
