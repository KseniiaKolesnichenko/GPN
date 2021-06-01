import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

import { Stepper, Search } from '../../components'

export const Main = () => (
    <Container>
        <Row className="justify-content-md-center">
            <Col lg={11}>
                <Stepper />
            </Col>
        </Row>
        <Row className="justify-content-md-center">
            <Col lg={11} className="mt-4">
                <Search />
            </Col>
        </Row>
    </Container>
)
