from selene import browser, have


class TextBox:
    def _fill_full_name(self, value):
        browser.element('#userName').type(value)
        return self

    def _fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def _fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def _fill_permanent_address(self, value):
        browser.element('#permanentAddress').type(value)
        return self

    def fill_form(self, full_name, email, current_address, permanent_address):
        self._fill_full_name(full_name)
        self._fill_email(email)
        self._fill_current_address(current_address)
        self._fill_permanent_address(permanent_address)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_be_registered(self, full_name, email, current_address, permanent_address):
        container = browser.element('#output')
        container.element('#name').should(have.text(full_name))
        container.element('#email').should(have.text(email))
        container.element('#currentAddress').should(have.text(current_address))
        container.element('#permanentAddress').should(have.text(permanent_address))
        return self

