"""Commands for the Storage domain (generated)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Literal, Optional

from ..mixins.datatype import DataType, FieldMeta, encode

if TYPE_CHECKING:
    from .types import (
        RelatedWebsiteSet,
        SerializedStorageKey,
        SharedStorageEntry,
        SharedStorageMetadata,
        StorageBucket,
        TrustTokens,
        UsageForType,
    )
    from ..browser.types import BrowserContextID as Browser_BrowserContextID
    from ..network.types import Cookie as Network_Cookie
    from ..network.types import CookieParam as Network_CookieParam
    from ..page.types import FrameId as Page_FrameId

@dataclass
class GetStorageKeyForFrameReturn(DataType):
    """Return value of :meth:`Storage.get_storage_key_for_frame`."""
    storage_key: SerializedStorageKey
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
    )


@dataclass
class GetStorageKeyReturn(DataType):
    """Return value of :meth:`Storage.get_storage_key`."""
    storage_key: SerializedStorageKey
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('storage_key', 'storageKey', False, 'primitive'),
    )


@dataclass
class GetCookiesReturn(DataType):
    """Return value of :meth:`Storage.get_cookies`."""
    cookies: List[Network_Cookie]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('cookies', 'cookies', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.Cookie')),
    )


@dataclass
class GetUsageAndQuotaReturn(DataType):
    """Return value of :meth:`Storage.get_usage_and_quota`."""
    usage: float
    quota: float
    override_active: bool
    usage_breakdown: List[UsageForType]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('usage', 'usage', False, 'primitive'),
        FieldMeta('quota', 'quota', False, 'primitive'),
        FieldMeta('override_active', 'overrideActive', False, 'primitive'),
        FieldMeta('usage_breakdown', 'usageBreakdown', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.UsageForType')),
    )


@dataclass
class GetTrustTokensReturn(DataType):
    """Return value of :meth:`Storage.get_trust_tokens`."""
    tokens: List[TrustTokens]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('tokens', 'tokens', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.TrustTokens')),
    )


@dataclass
class ClearTrustTokensReturn(DataType):
    """Return value of :meth:`Storage.clear_trust_tokens`."""
    did_delete_tokens: bool
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('did_delete_tokens', 'didDeleteTokens', False, 'primitive'),
    )


@dataclass
class GetInterestGroupDetailsReturn(DataType):
    """Return value of :meth:`Storage.get_interest_group_details`."""
    details: Dict[str, Any]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('details', 'details', False, 'primitive'),
    )


@dataclass
class GetSharedStorageMetadataReturn(DataType):
    """Return value of :meth:`Storage.get_shared_storage_metadata`."""
    metadata: SharedStorageMetadata
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('metadata', 'metadata', False, 'object', ref='Storage.SharedStorageMetadata'),
    )


@dataclass
class GetSharedStorageEntriesReturn(DataType):
    """Return value of :meth:`Storage.get_shared_storage_entries`."""
    entries: List[SharedStorageEntry]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('entries', 'entries', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.SharedStorageEntry')),
    )


@dataclass
class RunBounceTrackingMitigationsReturn(DataType):
    """Return value of :meth:`Storage.run_bounce_tracking_mitigations`."""
    deleted_sites: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('deleted_sites', 'deletedSites', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


@dataclass
class SendPendingAttributionReportsReturn(DataType):
    """Return value of :meth:`Storage.send_pending_attribution_reports`."""
    num_sent: int
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('num_sent', 'numSent', False, 'primitive'),
    )


@dataclass
class GetRelatedWebsiteSetsReturn(DataType):
    """Return value of :meth:`Storage.get_related_website_sets`."""
    sets: List[RelatedWebsiteSet]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('sets', 'sets', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Storage.RelatedWebsiteSet')),
    )


@dataclass
class GetAffectedUrlsForThirdPartyCookieMetadataReturn(DataType):
    """Return value of :meth:`Storage.get_affected_urls_for_third_party_cookie_metadata`."""
    matched_urls: List[str]
    __FIELDS__: ClassVar[tuple] = (
        FieldMeta('matched_urls', 'matchedUrls', False, 'array', inner=FieldMeta('', '', False, 'primitive')),
    )


class Storage:
    """Commands of the Storage domain, bound to a target."""

    def __init__(self, target: Any) -> None:
        self._target = target


    async def get_storage_key_for_frame(self, *, frame_id: Page_FrameId) -> GetStorageKeyForFrameReturn:
        """
        Returns a storage key given a frame id.
        Deprecated. Please use Storage.getStorageKey instead.
        
        .. deprecated::
        :param frame_id:
        """
        _params: Dict[str, Any] = {}
        _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Storage.getStorageKeyForFrame', _params)
        return GetStorageKeyForFrameReturn.from_json(_result)

    async def get_storage_key(self, *, frame_id: Optional[Page_FrameId] = None) -> GetStorageKeyReturn:
        """
        Returns storage key for the given frame. If no frame ID is provided,
        the storage key of the target executing this command is returned.
        :param frame_id:
        """
        _params: Dict[str, Any] = {}
        if frame_id is not None:
            _params['frameId'] = encode(FieldMeta('', '', False, 'primitive'), frame_id)
        _result = await self._target.send('Storage.getStorageKey', _params)
        return GetStorageKeyReturn.from_json(_result)

    async def clear_data_for_origin(self, *, origin: str, storage_types: str) -> None:
        """
        Clears storage for origin.
        :param origin: Security origin.
        :param storage_types: Comma separated list of StorageType to clear.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _params['storageTypes'] = encode(FieldMeta('', '', False, 'primitive'), storage_types)
        _result = await self._target.send('Storage.clearDataForOrigin', _params)
        return None

    async def clear_data_for_storage_key(self, *, storage_key: str, storage_types: str) -> None:
        """
        Clears storage for storage key.
        :param storage_key: Storage key.
        :param storage_types: Comma separated list of StorageType to clear.
        """
        _params: Dict[str, Any] = {}
        _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        _params['storageTypes'] = encode(FieldMeta('', '', False, 'primitive'), storage_types)
        _result = await self._target.send('Storage.clearDataForStorageKey', _params)
        return None

    async def get_cookies(self, *, browser_context_id: Optional[Browser_BrowserContextID] = None) -> GetCookiesReturn:
        """
        Returns all browser cookies.
        :param browser_context_id: Browser context to use when called on the browser endpoint.
        """
        _params: Dict[str, Any] = {}
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Storage.getCookies', _params)
        return GetCookiesReturn.from_json(_result)

    async def set_cookies(self, *, cookies: List[Network_CookieParam], browser_context_id: Optional[Browser_BrowserContextID] = None) -> None:
        """
        Sets given cookies.
        :param cookies: Cookies to be set.
        :param browser_context_id: Browser context to use when called on the browser endpoint.
        """
        _params: Dict[str, Any] = {}
        _params['cookies'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'object', ref='Network.CookieParam')), cookies)
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Storage.setCookies', _params)
        return None

    async def clear_cookies(self, *, browser_context_id: Optional[Browser_BrowserContextID] = None) -> None:
        """
        Clears cookies.
        :param browser_context_id: Browser context to use when called on the browser endpoint.
        """
        _params: Dict[str, Any] = {}
        if browser_context_id is not None:
            _params['browserContextId'] = encode(FieldMeta('', '', False, 'primitive'), browser_context_id)
        _result = await self._target.send('Storage.clearCookies', _params)
        return None

    async def get_usage_and_quota(self, *, origin: str) -> GetUsageAndQuotaReturn:
        """
        Returns usage and quota in bytes.
        :param origin: Security origin.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _result = await self._target.send('Storage.getUsageAndQuota', _params)
        return GetUsageAndQuotaReturn.from_json(_result)

    async def override_quota_for_origin(self, *, origin: str, quota_size: Optional[float] = None) -> None:
        """
        Override quota for the specified origin
        :param origin: Security origin.
        :param quota_size: The quota size (in bytes) to override the original quota with.
        If this is called multiple times, the overridden quota will be equal to
        the quotaSize provided in the final call. If this is called without
        specifying a quotaSize, the quota will be reset to the default value for
        the specified origin. If this is called multiple times with different
        origins, the override will be maintained for each origin until it is
        disabled (called without a quotaSize).
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        if quota_size is not None:
            _params['quotaSize'] = encode(FieldMeta('', '', False, 'primitive'), quota_size)
        _result = await self._target.send('Storage.overrideQuotaForOrigin', _params)
        return None

    async def track_cache_storage_for_origin(self, *, origin: str) -> None:
        """
        Registers origin to be notified when an update occurs to its cache storage list.
        :param origin: Security origin.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _result = await self._target.send('Storage.trackCacheStorageForOrigin', _params)
        return None

    async def track_cache_storage_for_storage_key(self, *, storage_key: str) -> None:
        """
        Registers storage key to be notified when an update occurs to its cache storage list.
        :param storage_key: Storage key.
        """
        _params: Dict[str, Any] = {}
        _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        _result = await self._target.send('Storage.trackCacheStorageForStorageKey', _params)
        return None

    async def track_indexed_db_for_origin(self, *, origin: str) -> None:
        """
        Registers origin to be notified when an update occurs to its IndexedDB.
        :param origin: Security origin.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _result = await self._target.send('Storage.trackIndexedDBForOrigin', _params)
        return None

    async def track_indexed_db_for_storage_key(self, *, storage_key: str) -> None:
        """
        Registers storage key to be notified when an update occurs to its IndexedDB.
        :param storage_key: Storage key.
        """
        _params: Dict[str, Any] = {}
        _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        _result = await self._target.send('Storage.trackIndexedDBForStorageKey', _params)
        return None

    async def untrack_cache_storage_for_origin(self, *, origin: str) -> None:
        """
        Unregisters origin from receiving notifications for cache storage.
        :param origin: Security origin.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _result = await self._target.send('Storage.untrackCacheStorageForOrigin', _params)
        return None

    async def untrack_cache_storage_for_storage_key(self, *, storage_key: str) -> None:
        """
        Unregisters storage key from receiving notifications for cache storage.
        :param storage_key: Storage key.
        """
        _params: Dict[str, Any] = {}
        _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        _result = await self._target.send('Storage.untrackCacheStorageForStorageKey', _params)
        return None

    async def untrack_indexed_db_for_origin(self, *, origin: str) -> None:
        """
        Unregisters origin from receiving notifications for IndexedDB.
        :param origin: Security origin.
        """
        _params: Dict[str, Any] = {}
        _params['origin'] = encode(FieldMeta('', '', False, 'primitive'), origin)
        _result = await self._target.send('Storage.untrackIndexedDBForOrigin', _params)
        return None

    async def untrack_indexed_db_for_storage_key(self, *, storage_key: str) -> None:
        """
        Unregisters storage key from receiving notifications for IndexedDB.
        :param storage_key: Storage key.
        """
        _params: Dict[str, Any] = {}
        _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        _result = await self._target.send('Storage.untrackIndexedDBForStorageKey', _params)
        return None

    async def get_trust_tokens(self) -> GetTrustTokensReturn:
        """
        Returns the number of stored Trust Tokens per issuer for the
        current browsing context.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Storage.getTrustTokens', _params)
        return GetTrustTokensReturn.from_json(_result)

    async def clear_trust_tokens(self, *, issuer_origin: str) -> ClearTrustTokensReturn:
        """
        Removes all Trust Tokens issued by the provided issuerOrigin.
        Leaves other stored data, including the issuer's Redemption Records, intact.
        :param issuer_origin:
        """
        _params: Dict[str, Any] = {}
        _params['issuerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), issuer_origin)
        _result = await self._target.send('Storage.clearTrustTokens', _params)
        return ClearTrustTokensReturn.from_json(_result)

    async def get_interest_group_details(self, *, owner_origin: str, name: str) -> GetInterestGroupDetailsReturn:
        """
        Gets details for a named interest group.
        :param owner_origin:
        :param name:
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _result = await self._target.send('Storage.getInterestGroupDetails', _params)
        return GetInterestGroupDetailsReturn.from_json(_result)

    async def set_interest_group_tracking(self, *, enable: bool) -> None:
        """
        Enables/Disables issuing of interestGroupAccessed events.
        :param enable:
        """
        _params: Dict[str, Any] = {}
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('Storage.setInterestGroupTracking', _params)
        return None

    async def set_interest_group_auction_tracking(self, *, enable: bool) -> None:
        """
        Enables/Disables issuing of interestGroupAuctionEventOccurred and
        interestGroupAuctionNetworkRequestCreated.
        :param enable:
        """
        _params: Dict[str, Any] = {}
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('Storage.setInterestGroupAuctionTracking', _params)
        return None

    async def get_shared_storage_metadata(self, *, owner_origin: str) -> GetSharedStorageMetadataReturn:
        """
        Gets metadata for an origin's shared storage.
        :param owner_origin:
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _result = await self._target.send('Storage.getSharedStorageMetadata', _params)
        return GetSharedStorageMetadataReturn.from_json(_result)

    async def get_shared_storage_entries(self, *, owner_origin: str) -> GetSharedStorageEntriesReturn:
        """
        Gets the entries in an given origin's shared storage.
        :param owner_origin:
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _result = await self._target.send('Storage.getSharedStorageEntries', _params)
        return GetSharedStorageEntriesReturn.from_json(_result)

    async def set_shared_storage_entry(self, *, owner_origin: str, key: str, value: str, ignore_if_present: Optional[bool] = None) -> None:
        """
        Sets entry with `key` and `value` for a given origin's shared storage.
        :param owner_origin:
        :param key:
        :param value:
        :param ignore_if_present: If `ignoreIfPresent` is included and true, then only sets the entry if
        `key` doesn't already exist.
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _params['key'] = encode(FieldMeta('', '', False, 'primitive'), key)
        _params['value'] = encode(FieldMeta('', '', False, 'primitive'), value)
        if ignore_if_present is not None:
            _params['ignoreIfPresent'] = encode(FieldMeta('', '', False, 'primitive'), ignore_if_present)
        _result = await self._target.send('Storage.setSharedStorageEntry', _params)
        return None

    async def delete_shared_storage_entry(self, *, owner_origin: str, key: str) -> None:
        """
        Deletes entry for `key` (if it exists) for a given origin's shared storage.
        :param owner_origin:
        :param key:
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _params['key'] = encode(FieldMeta('', '', False, 'primitive'), key)
        _result = await self._target.send('Storage.deleteSharedStorageEntry', _params)
        return None

    async def clear_shared_storage_entries(self, *, owner_origin: str) -> None:
        """
        Clears all entries for a given origin's shared storage.
        :param owner_origin:
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _result = await self._target.send('Storage.clearSharedStorageEntries', _params)
        return None

    async def reset_shared_storage_budget(self, *, owner_origin: str) -> None:
        """
        Resets the budget for `ownerOrigin` by clearing all budget withdrawals.
        :param owner_origin:
        """
        _params: Dict[str, Any] = {}
        _params['ownerOrigin'] = encode(FieldMeta('', '', False, 'primitive'), owner_origin)
        _result = await self._target.send('Storage.resetSharedStorageBudget', _params)
        return None

    async def set_shared_storage_tracking(self, *, enable: bool) -> None:
        """
        Enables/disables issuing of sharedStorageAccessed events.
        :param enable:
        """
        _params: Dict[str, Any] = {}
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('Storage.setSharedStorageTracking', _params)
        return None

    async def set_storage_bucket_tracking(self, *, storage_key: str, enable: bool) -> None:
        """
        Set tracking for a storage key's buckets.
        :param storage_key:
        :param enable:
        """
        _params: Dict[str, Any] = {}
        _params['storageKey'] = encode(FieldMeta('', '', False, 'primitive'), storage_key)
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('Storage.setStorageBucketTracking', _params)
        return None

    async def delete_storage_bucket(self, *, bucket: StorageBucket) -> None:
        """
        Deletes the Storage Bucket with the given storage key and bucket name.
        :param bucket:
        """
        _params: Dict[str, Any] = {}
        _params['bucket'] = encode(FieldMeta('', '', False, 'object', ref='Storage.StorageBucket'), bucket)
        _result = await self._target.send('Storage.deleteStorageBucket', _params)
        return None

    async def run_bounce_tracking_mitigations(self) -> RunBounceTrackingMitigationsReturn:
        """Deletes state for sites identified as potential bounce trackers, immediately."""
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Storage.runBounceTrackingMitigations', _params)
        return RunBounceTrackingMitigationsReturn.from_json(_result)

    async def set_attribution_reporting_local_testing_mode(self, *, enabled: bool) -> None:
        """
        https://wicg.github.io/attribution-reporting-api/
        :param enabled: If enabled, noise is suppressed and reports are sent immediately.
        """
        _params: Dict[str, Any] = {}
        _params['enabled'] = encode(FieldMeta('', '', False, 'primitive'), enabled)
        _result = await self._target.send('Storage.setAttributionReportingLocalTestingMode', _params)
        return None

    async def set_attribution_reporting_tracking(self, *, enable: bool) -> None:
        """
        Enables/disables issuing of Attribution Reporting events.
        :param enable:
        """
        _params: Dict[str, Any] = {}
        _params['enable'] = encode(FieldMeta('', '', False, 'primitive'), enable)
        _result = await self._target.send('Storage.setAttributionReportingTracking', _params)
        return None

    async def send_pending_attribution_reports(self) -> SendPendingAttributionReportsReturn:
        """
        Sends all pending Attribution Reports immediately, regardless of their
        scheduled report time.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Storage.sendPendingAttributionReports', _params)
        return SendPendingAttributionReportsReturn.from_json(_result)

    async def get_related_website_sets(self) -> GetRelatedWebsiteSetsReturn:
        """
        Returns the effective Related Website Sets in use by this profile for the browser
        session. The effective Related Website Sets will not change during a browser session.
        """
        _params: Dict[str, Any] = {}
        _result = await self._target.send('Storage.getRelatedWebsiteSets', _params)
        return GetRelatedWebsiteSetsReturn.from_json(_result)

    async def get_affected_urls_for_third_party_cookie_metadata(self, *, first_party_url: str, third_party_urls: List[str]) -> GetAffectedUrlsForThirdPartyCookieMetadataReturn:
        """
        Returns the list of URLs from a page and its embedded resources that match
        existing grace period URL pattern rules.
        https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period
        :param first_party_url: The URL of the page currently being visited.
        :param third_party_urls: The list of embedded resource URLs from the page.
        """
        _params: Dict[str, Any] = {}
        _params['firstPartyUrl'] = encode(FieldMeta('', '', False, 'primitive'), first_party_url)
        _params['thirdPartyUrls'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), third_party_urls)
        _result = await self._target.send('Storage.getAffectedUrlsForThirdPartyCookieMetadata', _params)
        return GetAffectedUrlsForThirdPartyCookieMetadataReturn.from_json(_result)

    async def set_protected_audience_k_anonymity(self, *, owner: str, name: str, hashes: List[str]) -> None:
        """
        :param owner:
        :param name:
        :param hashes:
        """
        _params: Dict[str, Any] = {}
        _params['owner'] = encode(FieldMeta('', '', False, 'primitive'), owner)
        _params['name'] = encode(FieldMeta('', '', False, 'primitive'), name)
        _params['hashes'] = encode(FieldMeta('', '', False, 'array', inner=FieldMeta('', '', False, 'primitive')), hashes)
        _result = await self._target.send('Storage.setProtectedAudienceKAnonymity', _params)
        return None
