"""Custom types and enums for the FedCm domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, register


@register("FedCm.LoginState")
class LoginState(str, Enum):
    """
    Whether this is a sign-up or sign-in action for this account, i.e.
    whether this account has ever been used to sign in to this RP before.
    """
    SIGNIN = 'SignIn'
    SIGNUP = 'SignUp'


@register("FedCm.DialogType")
class DialogType(str, Enum):
    """The types of FedCM dialogs."""
    ACCOUNTCHOOSER = 'AccountChooser'
    AUTOREAUTHN = 'AutoReauthn'
    CONFIRMIDPLOGIN = 'ConfirmIdpLogin'
    ERROR = 'Error'


@register("FedCm.DialogButton")
class DialogButton(str, Enum):
    """The buttons on the FedCM dialog."""
    CONFIRMIDPLOGINCONTINUE = 'ConfirmIdpLoginContinue'
    ERRORGOTIT = 'ErrorGotIt'
    ERRORMOREDETAILS = 'ErrorMoreDetails'


@register("FedCm.AccountUrlType")
class AccountUrlType(str, Enum):
    """The URLs that each account has"""
    TERMSOFSERVICE = 'TermsOfService'
    PRIVACYPOLICY = 'PrivacyPolicy'


@register("FedCm.Account")
@dataclass
class Account(DataType):
    """Corresponds to IdentityRequestAccount"""
    account_id: str
    email: str
    name: str
    given_name: str
    picture_url: str
    idp_config_url: str
    idp_login_url: str
    login_state: LoginState
    terms_of_service_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('account_id', 'accountId', False, 'primitive'),
        FieldMeta('email', 'email', False, 'primitive'),
        FieldMeta('name', 'name', False, 'primitive'),
        FieldMeta('given_name', 'givenName', False, 'primitive'),
        FieldMeta('picture_url', 'pictureUrl', False, 'primitive'),
        FieldMeta('idp_config_url', 'idpConfigUrl', False, 'primitive'),
        FieldMeta('idp_login_url', 'idpLoginUrl', False, 'primitive'),
        FieldMeta('login_state', 'loginState', False, 'enum', ref='FedCm.LoginState'),
        FieldMeta('terms_of_service_url', 'termsOfServiceUrl', True, 'primitive'),
        FieldMeta('privacy_policy_url', 'privacyPolicyUrl', True, 'primitive'),
    )

__all__ = ["Account", "AccountUrlType", "DialogButton", "DialogType", "LoginState"]
