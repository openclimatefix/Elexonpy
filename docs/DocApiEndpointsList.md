## Documentation for API Endpoints

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AvailabilityApi* | [**generation_availability_summary14_d_get**](./AvailabilityApi.md#generation_availability_summary14_d_get) | **GET** /generation/availability/summary/14D | Fourteen-day generation forecast
*AvailabilityApi* | [**generation_availability_summary3_yw_get**](./AvailabilityApi.md#generation_availability_summary3_yw_get) | **GET** /generation/availability/summary/3YW | Three-year generation forecast
*BalancingMechanismDynamicApi* | [**balancing_dynamic_all_get**](./BalancingMechanismDynamicApi.md#balancing_dynamic_all_get) | **GET** /balancing/dynamic/all | Market-wide dynamic data (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
*BalancingMechanismDynamicApi* | [**balancing_dynamic_get**](./BalancingMechanismDynamicApi.md#balancing_dynamic_get) | **GET** /balancing/dynamic | Dynamic data per BMU (SEL, SIL, MZT, MNZT, MDV, MDP, NTB, NTO, NDZ)
*BalancingMechanismDynamicApi* | [**balancing_dynamic_rates_all_get**](./BalancingMechanismDynamicApi.md#balancing_dynamic_rates_all_get) | **GET** /balancing/dynamic/rates/all | Market-wide rate data (RDRE, RURE, RDRI, RURI)
*BalancingMechanismDynamicApi* | [**balancing_dynamic_rates_get**](./BalancingMechanismDynamicApi.md#balancing_dynamic_rates_get) | **GET** /balancing/dynamic/rates | Rate data per BMU (RDRE, RURE, RDRI, RURI)
*BalancingMechanismPhysicalApi* | [**balancing_physical_all_get**](./BalancingMechanismPhysicalApi.md#balancing_physical_all_get) | **GET** /balancing/physical/all | Market-wide physical data (PN, QPN, MILS, MELS)
*BalancingMechanismPhysicalApi* | [**balancing_physical_get**](./BalancingMechanismPhysicalApi.md#balancing_physical_get) | **GET** /balancing/physical | Physical data per BMU (PN, QPN, MILS, MELS)
*BalancingServicesAdjustmentDisaggregatedApi* | [**balancing_nonbm_disbsad_details_get**](./BalancingServicesAdjustmentDisaggregatedApi.md#balancing_nonbm_disbsad_details_get) | **GET** /balancing/nonbm/disbsad/details | Disaggregated balancing services adjustment per settlement period (DISBSAD)
*BalancingServicesAdjustmentDisaggregatedApi* | [**balancing_nonbm_disbsad_summary_get**](./BalancingServicesAdjustmentDisaggregatedApi.md#balancing_nonbm_disbsad_summary_get) | **GET** /balancing/nonbm/disbsad/summary | Disaggregated balancing services adjustment time series (DISBSAD)
*BalancingServicesAdjustmentNetApi* | [**balancing_nonbm_netbsad_events_get**](./BalancingServicesAdjustmentNetApi.md#balancing_nonbm_netbsad_events_get) | **GET** /balancing/nonbm/netbsad/events | Net balancing services adjustment events (NETBSAD)
*BalancingServicesAdjustmentNetApi* | [**balancing_nonbm_netbsad_get**](./BalancingServicesAdjustmentNetApi.md#balancing_nonbm_netbsad_get) | **GET** /balancing/nonbm/netbsad | Net balancing services adjustment time series (NETBSAD)
*BidOfferApi* | [**balancing_bid_offer_all_get**](./BidOfferApi.md#balancing_bid_offer_all_get) | **GET** /balancing/bid-offer/all | Market-wide bid-offer data (BOD)
*BidOfferApi* | [**balancing_bid_offer_get**](./BidOfferApi.md#balancing_bid_offer_get) | **GET** /balancing/bid-offer | Bid-offer data per BMU (BOD)
*BidOfferAcceptancesApi* | [**balancing_acceptances_all_get**](./BidOfferAcceptancesApi.md#balancing_acceptances_all_get) | **GET** /balancing/acceptances/all | Market-wide bid-offer acceptances (BOALF)
*BidOfferAcceptancesApi* | [**balancing_acceptances_all_latest_get**](./BidOfferAcceptancesApi.md#balancing_acceptances_all_latest_get) | **GET** /balancing/acceptances/all/latest | Latest market-wide bid-offer acceptances (BOALF)
*BidOfferAcceptancesApi* | [**balancing_acceptances_get**](./BidOfferAcceptancesApi.md#balancing_acceptances_get) | **GET** /balancing/acceptances | Bid-offer acceptances per BMU (BOALF)
*CreditDefaultNoticeApi* | [**c_dn_get**](./CreditDefaultNoticeApi.md#c_dn_get) | **GET** /CDN | [DEPRECATED] Credit default notices (CDN)
*DatasetsApi* | [**datasets_abuc_get**](./DatasetsApi.md#datasets_abuc_get) | **GET** /datasets/ABUC | Amount Of Balancing Reserves Under Contract (ABUC / B1720)
*DatasetsApi* | [**datasets_abuc_stream_get**](./DatasetsApi.md#datasets_abuc_stream_get) | **GET** /datasets/ABUC/stream | Amount Of Balancing Reserves Under Contract (ABUC / B1720) stream
*DatasetsApi* | [**datasets_agpt_get**](./DatasetsApi.md#datasets_agpt_get) | **GET** /datasets/AGPT | Actual Aggregated Generation Per Type (AGPT / B1620)
*DatasetsApi* | [**datasets_agpt_stream_get**](./DatasetsApi.md#datasets_agpt_stream_get) | **GET** /datasets/AGPT/stream | Actual Aggregated Generation Per Type (AGPT / B1620) stream
*DatasetsApi* | [**datasets_agws_get**](./DatasetsApi.md#datasets_agws_get) | **GET** /datasets/AGWS | Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630)
*DatasetsApi* | [**datasets_agws_stream_get**](./DatasetsApi.md#datasets_agws_stream_get) | **GET** /datasets/AGWS/stream | Actual Or Estimated Wind And Solar Power Generation (AGWS / B1630) stream
*DatasetsApi* | [**datasets_aobe_get**](./DatasetsApi.md#datasets_aobe_get) | **GET** /datasets/AOBE | Accepted Offered Balancing Energy (AOBE)
*DatasetsApi* | [**datasets_aobe_stream_get**](./DatasetsApi.md#datasets_aobe_stream_get) | **GET** /datasets/AOBE/stream | Accepted Offered Balancing Energy (AOBE) stream
*DatasetsApi* | [**datasets_atl_get**](./DatasetsApi.md#datasets_atl_get) | **GET** /datasets/ATL | Actual Total Load Per Bidding Zone (ATL / B0610)
*DatasetsApi* | [**datasets_atl_stream_get**](./DatasetsApi.md#datasets_atl_stream_get) | **GET** /datasets/ATL/stream | Actual Total Load Per Bidding Zone (ATL / B0610) stream
*DatasetsApi* | [**datasets_b1610_get**](./DatasetsApi.md#datasets_b1610_get) | **GET** /datasets/B1610 | Actual Generation Output Per Generation Unit (B1610)
*DatasetsApi* | [**datasets_b1610_stream_get**](./DatasetsApi.md#datasets_b1610_stream_get) | **GET** /datasets/B1610/stream | Actual Generation Output Per Generation Unit (B1610) stream
*DatasetsApi* | [**datasets_beb_get**](./DatasetsApi.md#datasets_beb_get) | **GET** /datasets/BEB | Balancing Energy Bids (BEB)
*DatasetsApi* | [**datasets_beb_stream_get**](./DatasetsApi.md#datasets_beb_stream_get) | **GET** /datasets/BEB/stream | Balancing Energy Bids (BEB) stream
*DatasetsApi* | [**datasets_boalf_get**](./DatasetsApi.md#datasets_boalf_get) | **GET** /datasets/BOALF | Bid Offer Acceptance Level Flagged (BOALF)
*DatasetsApi* | [**datasets_boalf_stream_get**](./DatasetsApi.md#datasets_boalf_stream_get) | **GET** /datasets/BOALF/stream | Bid Offer Acceptance Level Flagged (BOALF) stream
*DatasetsApi* | [**datasets_bod_get**](./DatasetsApi.md#datasets_bod_get) | **GET** /datasets/BOD | Bid Offer Data (BOD)
*DatasetsApi* | [**datasets_bod_stream_get**](./DatasetsApi.md#datasets_bod_stream_get) | **GET** /datasets/BOD/stream | Bid-Offer Data (BOD) stream
*DatasetsApi* | [**datasets_cbs_get**](./DatasetsApi.md#datasets_cbs_get) | **GET** /datasets/CBS | Current Balancing State (CBS)
*DatasetsApi* | [**datasets_cbs_stream_get**](./DatasetsApi.md#datasets_cbs_stream_get) | **GET** /datasets/CBS/stream | Current Balancing State (CBS) stream
*DatasetsApi* | [**datasets_ccm_get**](./DatasetsApi.md#datasets_ccm_get) | **GET** /datasets/CCM | Cost of Congestion Management (CCM / B1330)
*DatasetsApi* | [**datasets_ccm_stream_get**](./DatasetsApi.md#datasets_ccm_stream_get) | **GET** /datasets/CCM/stream | Cost of Congestion Management (CCM / B1330) stream
*DatasetsApi* | [**datasets_cdn_get**](./DatasetsApi.md#datasets_cdn_get) | **GET** /datasets/CDN | Credit default notices (CDN)
*DatasetsApi* | [**datasets_cdn_stream_get**](./DatasetsApi.md#datasets_cdn_stream_get) | **GET** /datasets/CDN/stream | Credit default notices (CDN)
*DatasetsApi* | [**datasets_dag_get**](./DatasetsApi.md#datasets_dag_get) | **GET** /datasets/DAG | Day-Ahead Aggregated Generation (DAG / B1430)
*DatasetsApi* | [**datasets_dag_stream_get**](./DatasetsApi.md#datasets_dag_stream_get) | **GET** /datasets/DAG/stream | Day-Ahead Aggregated Generation (DAG / B1430) stream
*DatasetsApi* | [**datasets_datl_get**](./DatasetsApi.md#datasets_datl_get) | **GET** /datasets/DATL | Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620)
*DatasetsApi* | [**datasets_datl_stream_get**](./DatasetsApi.md#datasets_datl_stream_get) | **GET** /datasets/DATL/stream | Day-Ahead Total Load Forecast Per Bidding Zone (DATL / B0620) stream
*DatasetsApi* | [**datasets_dci_get**](./DatasetsApi.md#datasets_dci_get) | **GET** /datasets/DCI | Demand control instructions (DCI)
*DatasetsApi* | [**datasets_dci_stream_get**](./DatasetsApi.md#datasets_dci_stream_get) | **GET** /datasets/DCI/stream | Demand control instructions (DCI) stream
*DatasetsApi* | [**datasets_dgws_get**](./DatasetsApi.md#datasets_dgws_get) | **GET** /datasets/DGWS | Day-Ahead Generation For Wind And Solar (DGWS / B1440)
*DatasetsApi* | [**datasets_dgws_stream_get**](./DatasetsApi.md#datasets_dgws_stream_get) | **GET** /datasets/DGWS/stream | Day-Ahead Generation For Wind And Solar (DGWS / B1440) stream
*DatasetsApi* | [**datasets_disbsad_get**](./DatasetsApi.md#datasets_disbsad_get) | **GET** /datasets/DISBSAD | Disaggregated Balancing Services Adjustment Data (DISBSAD)
*DatasetsApi* | [**datasets_disbsad_stream_get**](./DatasetsApi.md#datasets_disbsad_stream_get) | **GET** /datasets/DISBSAD/stream | Disaggregated Balancing Services Adjustment Data (DISBSAD) stream
*DatasetsApi* | [**datasets_feib_get**](./DatasetsApi.md#datasets_feib_get) | **GET** /datasets/FEIB | Financial Expenses and Income for Balancing (FEIB / B1790)
*DatasetsApi* | [**datasets_feib_stream_get**](./DatasetsApi.md#datasets_feib_stream_get) | **GET** /datasets/FEIB/stream | Financial Expenses and Income for Balancing (FEIB / B1790) stream
*DatasetsApi* | [**datasets_fou2_t14_d_get**](./DatasetsApi.md#datasets_fou2_t14_d_get) | **GET** /datasets/FOU2T14D | 2 to 14 days ahead generation availability aggregated by fuel type (FOU2T14D)
*DatasetsApi* | [**datasets_fou2_t3_yw_get**](./DatasetsApi.md#datasets_fou2_t3_yw_get) | **GET** /datasets/FOU2T3YW | 2 to 156 weeks ahead generation availability aggregated by fuel type (FOU2T3YW)
*DatasetsApi* | [**datasets_freq_get**](./DatasetsApi.md#datasets_freq_get) | **GET** /datasets/FREQ | System frequency (FREQ)
*DatasetsApi* | [**datasets_freq_stream_get**](./DatasetsApi.md#datasets_freq_stream_get) | **GET** /datasets/FREQ/stream | System frequency (FREQ) stream
*DatasetsApi* | [**datasets_fuelhh_get**](./DatasetsApi.md#datasets_fuelhh_get) | **GET** /datasets/FUELHH | Half-hourly generation outturn by fuel type (FUELHH)
*DatasetsApi* | [**datasets_fuelhh_stream_get**](./DatasetsApi.md#datasets_fuelhh_stream_get) | **GET** /datasets/FUELHH/stream | Half-hourly generation outturn by fuel type (FUELHH) stream
*DatasetsApi* | [**datasets_fuelinst_get**](./DatasetsApi.md#datasets_fuelinst_get) | **GET** /datasets/FUELINST | Instantaneous generation outturn by fuel type (FUELINST)
*DatasetsApi* | [**datasets_fuelinst_stream_get**](./DatasetsApi.md#datasets_fuelinst_stream_get) | **GET** /datasets/FUELINST/stream | Instantaneous generation outturn by fuel type (FUELINST) stream
*DatasetsApi* | [**datasets_igca_get**](./DatasetsApi.md#datasets_igca_get) | **GET** /datasets/IGCA | Installed Generation Capacity Aggregated (IGCA / B1410)
*DatasetsApi* | [**datasets_igca_stream_get**](./DatasetsApi.md#datasets_igca_stream_get) | **GET** /datasets/IGCA/stream | Installed Generation Capacity Aggregated (IGCA / B1410) stream
*DatasetsApi* | [**datasets_igcpu_get**](./DatasetsApi.md#datasets_igcpu_get) | **GET** /datasets/IGCPU | Installed Generation Capacity per Unit (IGCPU / B1420)
*DatasetsApi* | [**datasets_igcpu_stream_get**](./DatasetsApi.md#datasets_igcpu_stream_get) | **GET** /datasets/IGCPU/stream | Installed Generation Capacity per Unit (IGCPU / B1420) stream
*DatasetsApi* | [**datasets_imbalngc_get**](./DatasetsApi.md#datasets_imbalngc_get) | **GET** /datasets/IMBALNGC | Day and day-ahead indicated imbalance (IMBALNGC)
*DatasetsApi* | [**datasets_imbalngc_stream_get**](./DatasetsApi.md#datasets_imbalngc_stream_get) | **GET** /datasets/IMBALNGC/stream | Day and day-ahead indicated imbalance (IMBALNGC) stream
*DatasetsApi* | [**datasets_inddem_get**](./DatasetsApi.md#datasets_inddem_get) | **GET** /datasets/INDDEM | Day and day-ahead indicated demand (INDDEM)
*DatasetsApi* | [**datasets_inddem_stream_get**](./DatasetsApi.md#datasets_inddem_stream_get) | **GET** /datasets/INDDEM/stream | Day and day-ahead indicated demand (INDDEM) stream
*DatasetsApi* | [**datasets_indgen_get**](./DatasetsApi.md#datasets_indgen_get) | **GET** /datasets/INDGEN | Day and day-ahead indicated generation (INDGEN)
*DatasetsApi* | [**datasets_indgen_stream_get**](./DatasetsApi.md#datasets_indgen_stream_get) | **GET** /datasets/INDGEN/stream | Day and day-ahead indicated generation (INDGEN) stream
*DatasetsApi* | [**datasets_indo_get**](./DatasetsApi.md#datasets_indo_get) | **GET** /datasets/INDO | Initial National Demand outturn (INDO)
*DatasetsApi* | [**datasets_indod_get**](./DatasetsApi.md#datasets_indod_get) | **GET** /datasets/INDOD | Initial National Demand outturn daily (INDOD)
*DatasetsApi* | [**datasets_indod_stream_get**](./DatasetsApi.md#datasets_indod_stream_get) | **GET** /datasets/INDOD/stream | Initial National Demand outturn daily (INDOD) stream
*DatasetsApi* | [**datasets_itsdo_get**](./DatasetsApi.md#datasets_itsdo_get) | **GET** /datasets/ITSDO | Initial Transmission System Demand outturn (ITSDO)
*DatasetsApi* | [**datasets_lolpdrm_get**](./DatasetsApi.md#datasets_lolpdrm_get) | **GET** /datasets/LOLPDRM | Loss of load probability and de-rated margin (LOLPDRM)
*DatasetsApi* | [**datasets_lolpdrm_stream_get**](./DatasetsApi.md#datasets_lolpdrm_stream_get) | **GET** /datasets/LOLPDRM/stream | Loss of load probability and de-rated margin (LOLPDRM)
*DatasetsApi* | [**datasets_matl_get**](./DatasetsApi.md#datasets_matl_get) | **GET** /datasets/MATL | Month-Ahead Total Load Forecast Per Bidding Zone (MATL / B0640)
*DatasetsApi* | [**datasets_matl_stream_get**](./DatasetsApi.md#datasets_matl_stream_get) | **GET** /datasets/MATL/stream | Month-Ahead Total Load Forecast Per Bidding Zone (MATL / B0640) stream
*DatasetsApi* | [**datasets_mdp_get**](./DatasetsApi.md#datasets_mdp_get) | **GET** /datasets/MDP | Maximum Delivery Period (MDP)
*DatasetsApi* | [**datasets_mdp_stream_get**](./DatasetsApi.md#datasets_mdp_stream_get) | **GET** /datasets/MDP/stream | Maximum Delivery Period (MDP) stream
*DatasetsApi* | [**datasets_mdv_get**](./DatasetsApi.md#datasets_mdv_get) | **GET** /datasets/MDV | Maximum Delivery Volume (MDV)
*DatasetsApi* | [**datasets_mdv_stream_get**](./DatasetsApi.md#datasets_mdv_stream_get) | **GET** /datasets/MDV/stream | Maximum Delivery Volume (MDV) stream
*DatasetsApi* | [**datasets_melngc_get**](./DatasetsApi.md#datasets_melngc_get) | **GET** /datasets/MELNGC | Day and day-ahead indicated margin (MELNGC)
*DatasetsApi* | [**datasets_melngc_stream_get**](./DatasetsApi.md#datasets_melngc_stream_get) | **GET** /datasets/MELNGC/stream | Day and day-ahead indicated margin (MELNGC) stream
*DatasetsApi* | [**datasets_mels_get**](./DatasetsApi.md#datasets_mels_get) | **GET** /datasets/MELS | Maximum Export Limit (MELS)
*DatasetsApi* | [**datasets_mels_stream_get**](./DatasetsApi.md#datasets_mels_stream_get) | **GET** /datasets/MELS/stream | Maximum Export Limit (MELS) stream
*DatasetsApi* | [**datasets_metadata_latest_get**](./DatasetsApi.md#datasets_metadata_latest_get) | **GET** /datasets/metadata/latest | Returns the time when each dataset was last updated
*DatasetsApi* | [**datasets_mid_get**](./DatasetsApi.md#datasets_mid_get) | **GET** /datasets/MID | Market Index Data (MID)
*DatasetsApi* | [**datasets_mid_stream_get**](./DatasetsApi.md#datasets_mid_stream_get) | **GET** /datasets/MID/stream | Market Index Data (MID) stream
*DatasetsApi* | [**datasets_mils_get**](./DatasetsApi.md#datasets_mils_get) | **GET** /datasets/MILS | Maximum Import Limit (MILS)
*DatasetsApi* | [**datasets_mils_stream_get**](./DatasetsApi.md#datasets_mils_stream_get) | **GET** /datasets/MILS/stream | Maximum Import Limit (MILS) stream
*DatasetsApi* | [**datasets_mnzt_get**](./DatasetsApi.md#datasets_mnzt_get) | **GET** /datasets/MNZT | Minimum Non-Zero Time (MNZT)
*DatasetsApi* | [**datasets_mnzt_stream_get**](./DatasetsApi.md#datasets_mnzt_stream_get) | **GET** /datasets/MNZT/stream | Minimum Non-Zero Time (MNZT) stream
*DatasetsApi* | [**datasets_mzt_get**](./DatasetsApi.md#datasets_mzt_get) | **GET** /datasets/MZT | Minimum Zero Time (MZT)
*DatasetsApi* | [**datasets_mzt_stream_get**](./DatasetsApi.md#datasets_mzt_stream_get) | **GET** /datasets/MZT/stream | Minimum Zero Time (MZT) stream
*DatasetsApi* | [**datasets_ndf_get**](./DatasetsApi.md#datasets_ndf_get) | **GET** /datasets/NDF | Day and day-ahead National Demand forecast (NDF)
*DatasetsApi* | [**datasets_ndf_stream_get**](./DatasetsApi.md#datasets_ndf_stream_get) | **GET** /datasets/NDF/stream | Day and day-ahead National Demand forecast (NDF) stream
*DatasetsApi* | [**datasets_ndfd_get**](./DatasetsApi.md#datasets_ndfd_get) | **GET** /datasets/NDFD | 2-14 days ahead National Demand and surplus forecast (NDFD)
*DatasetsApi* | [**datasets_ndfd_stream_get**](./DatasetsApi.md#datasets_ndfd_stream_get) | **GET** /datasets/NDFD/stream | 2-14 days ahead National Demand and surplus forecast (NDFD) stream
*DatasetsApi* | [**datasets_ndfw_get**](./DatasetsApi.md#datasets_ndfw_get) | **GET** /datasets/NDFW | 2-52 weeks ahead National Demand and surplus forecast (NDFW)
*DatasetsApi* | [**datasets_ndfw_stream_get**](./DatasetsApi.md#datasets_ndfw_stream_get) | **GET** /datasets/NDFW/stream | 2-52 weeks ahead National Demand and surplus forecast (NDFW) stream
*DatasetsApi* | [**datasets_ndz_get**](./DatasetsApi.md#datasets_ndz_get) | **GET** /datasets/NDZ | Notice to Deviate from Zero (NDZ)
*DatasetsApi* | [**datasets_ndz_stream_get**](./DatasetsApi.md#datasets_ndz_stream_get) | **GET** /datasets/NDZ/stream | Notice to Deviate from Zero (NDZ) stream
*DatasetsApi* | [**datasets_netbsad_get**](./DatasetsApi.md#datasets_netbsad_get) | **GET** /datasets/NETBSAD | Net Balancing Services Adjustment Data (NETBSAD)
*DatasetsApi* | [**datasets_netbsad_stream_get**](./DatasetsApi.md#datasets_netbsad_stream_get) | **GET** /datasets/NETBSAD/stream | Net Balancing Services Adjustment Data (NETBSAD)
*DatasetsApi* | [**datasets_nonbm_get**](./DatasetsApi.md#datasets_nonbm_get) | **GET** /datasets/NONBM | Non-BM STOR (NONBM)
*DatasetsApi* | [**datasets_nonbm_stream_get**](./DatasetsApi.md#datasets_nonbm_stream_get) | **GET** /datasets/NONBM/stream | Non-BM STOR (NONBM) stream
*DatasetsApi* | [**datasets_nou2_t14_d_get**](./DatasetsApi.md#datasets_nou2_t14_d_get) | **GET** /datasets/NOU2T14D | 2 to 14 days ahead generation availability aggregated data (NOU2T14D)
*DatasetsApi* | [**datasets_nou2_t3_yw_get**](./DatasetsApi.md#datasets_nou2_t3_yw_get) | **GET** /datasets/NOU2T3YW | 2 to 156 weeks ahead generation availability aggregated data (NOU2T3YW)
*DatasetsApi* | [**datasets_ntb_get**](./DatasetsApi.md#datasets_ntb_get) | **GET** /datasets/NTB | Notice to Deliver Bids (NTB)
*DatasetsApi* | [**datasets_ntb_stream_get**](./DatasetsApi.md#datasets_ntb_stream_get) | **GET** /datasets/NTB/stream | Notice to Deliver Bids (NTB) stream
*DatasetsApi* | [**datasets_nto_get**](./DatasetsApi.md#datasets_nto_get) | **GET** /datasets/NTO | Notice to Deliver Offers (NTO)
*DatasetsApi* | [**datasets_nto_stream_get**](./DatasetsApi.md#datasets_nto_stream_get) | **GET** /datasets/NTO/stream | Notice to Deliver Offers (NTO) stream
*DatasetsApi* | [**datasets_ocnmf3_y2_get**](./DatasetsApi.md#datasets_ocnmf3_y2_get) | **GET** /datasets/OCNMF3Y2 | 2-156 weeks ahead demand margin forecast (OCNMF3Y2)
*DatasetsApi* | [**datasets_ocnmf3_y2_stream_get**](./DatasetsApi.md#datasets_ocnmf3_y2_stream_get) | **GET** /datasets/OCNMF3Y2/stream | 2-156 weeks ahead demand margin forecast (OCNMF3Y2) stream
*DatasetsApi* | [**datasets_ocnmf3_y_get**](./DatasetsApi.md#datasets_ocnmf3_y_get) | **GET** /datasets/OCNMF3Y | 2-156 weeks ahead demand surplus forecast (OCNMF3Y)
*DatasetsApi* | [**datasets_ocnmf3_y_stream_get**](./DatasetsApi.md#datasets_ocnmf3_y_stream_get) | **GET** /datasets/OCNMF3Y/stream | 2-156 weeks ahead demand surplus forecast (OCNMF3Y) stream
*DatasetsApi* | [**datasets_ocnmfd2_get**](./DatasetsApi.md#datasets_ocnmfd2_get) | **GET** /datasets/OCNMFD2 | 2-14 days ahead demand margin forecast (OCNMFD2)
*DatasetsApi* | [**datasets_ocnmfd2_stream_get**](./DatasetsApi.md#datasets_ocnmfd2_stream_get) | **GET** /datasets/OCNMFD2/stream | 2-14 days ahead demand margin forecast (OCNMFD2) stream
*DatasetsApi* | [**datasets_ocnmfd_get**](./DatasetsApi.md#datasets_ocnmfd_get) | **GET** /datasets/OCNMFD | 2-14 days ahead demand surplus forecast (OCNMFD)
*DatasetsApi* | [**datasets_ocnmfd_stream_get**](./DatasetsApi.md#datasets_ocnmfd_stream_get) | **GET** /datasets/OCNMFD/stream | 2-14 days ahead demand surplus forecast (OCNMFD) stream
*DatasetsApi* | [**datasets_pbc_get**](./DatasetsApi.md#datasets_pbc_get) | **GET** /datasets/PBC | Procured Balancing Capacity (PBC)
*DatasetsApi* | [**datasets_pbc_stream_get**](./DatasetsApi.md#datasets_pbc_stream_get) | **GET** /datasets/PBC/stream | Procured Balancing Capacity (PBC) stream
*DatasetsApi* | [**datasets_pn_get**](./DatasetsApi.md#datasets_pn_get) | **GET** /datasets/PN | Physical Notifications (PN)
*DatasetsApi* | [**datasets_pn_stream_get**](./DatasetsApi.md#datasets_pn_stream_get) | **GET** /datasets/PN/stream | Physical Notifications (PN) stream
*DatasetsApi* | [**datasets_ppbr_get**](./DatasetsApi.md#datasets_ppbr_get) | **GET** /datasets/PPBR | Prices Of Procured Balancing Reserves (PPBR / B1730)
*DatasetsApi* | [**datasets_ppbr_stream_get**](./DatasetsApi.md#datasets_ppbr_stream_get) | **GET** /datasets/PPBR/stream | Prices Of Procured Balancing Reserves (PPBR / B1730) stream
*DatasetsApi* | [**datasets_qas_get**](./DatasetsApi.md#datasets_qas_get) | **GET** /datasets/QAS | Balancing Services Volume (QAS)
*DatasetsApi* | [**datasets_qas_stream_get**](./DatasetsApi.md#datasets_qas_stream_get) | **GET** /datasets/QAS/stream | Balancing Services Volume (QAS) stream
*DatasetsApi* | [**datasets_qpn_get**](./DatasetsApi.md#datasets_qpn_get) | **GET** /datasets/QPN | Quiescent Physical Notifications (QPN)
*DatasetsApi* | [**datasets_qpn_stream_get**](./DatasetsApi.md#datasets_qpn_stream_get) | **GET** /datasets/QPN/stream | Quiescent Physical Notifications (QPN) stream
*DatasetsApi* | [**datasets_rdre_get**](./DatasetsApi.md#datasets_rdre_get) | **GET** /datasets/RDRE | Run Down Rate Export (RDRE)
*DatasetsApi* | [**datasets_rdre_stream_get**](./DatasetsApi.md#datasets_rdre_stream_get) | **GET** /datasets/RDRE/stream | Run Down Rate Export (RDRE) stream
*DatasetsApi* | [**datasets_rdri_get**](./DatasetsApi.md#datasets_rdri_get) | **GET** /datasets/RDRI | Run Down Rate Import (RDRI)
*DatasetsApi* | [**datasets_rdri_stream_get**](./DatasetsApi.md#datasets_rdri_stream_get) | **GET** /datasets/RDRI/stream | Run Down Rate Import (RDRI) stream
*DatasetsApi* | [**datasets_remit_get**](./DatasetsApi.md#datasets_remit_get) | **GET** /datasets/REMIT | The Regulation on Wholesale Energy Markets Integrity and Transparency (REMIT)
*DatasetsApi* | [**datasets_remit_stream_get**](./DatasetsApi.md#datasets_remit_stream_get) | **GET** /datasets/REMIT/stream | The Regulation on Wholesale Energy Markets Integrity and Transparency (REMIT) stream
*DatasetsApi* | [**datasets_rure_get**](./DatasetsApi.md#datasets_rure_get) | **GET** /datasets/RURE | Run Up Rate Export (RURE)
*DatasetsApi* | [**datasets_rure_stream_get**](./DatasetsApi.md#datasets_rure_stream_get) | **GET** /datasets/RURE/stream | Run Up Rate Export (RURE) stream
*DatasetsApi* | [**datasets_ruri_get**](./DatasetsApi.md#datasets_ruri_get) | **GET** /datasets/RURI | Run Up Rate Import (RURI)
*DatasetsApi* | [**datasets_ruri_stream_get**](./DatasetsApi.md#datasets_ruri_stream_get) | **GET** /datasets/RURI/stream | Run Up Rate Import (RURI) stream
*DatasetsApi* | [**datasets_sel_get**](./DatasetsApi.md#datasets_sel_get) | **GET** /datasets/SEL | Stable Export Limit (SEL)
*DatasetsApi* | [**datasets_sel_stream_get**](./DatasetsApi.md#datasets_sel_stream_get) | **GET** /datasets/SEL/stream | Stable Export Limit (SEL) stream
*DatasetsApi* | [**datasets_sil_get**](./DatasetsApi.md#datasets_sil_get) | **GET** /datasets/SIL | Stable Import Limit (SIL)
*DatasetsApi* | [**datasets_sil_stream_get**](./DatasetsApi.md#datasets_sil_stream_get) | **GET** /datasets/SIL/stream | Stable Import Limit (SIL) stream
*DatasetsApi* | [**datasets_soso_get**](./DatasetsApi.md#datasets_soso_get) | **GET** /datasets/SOSO | SO-SO prices (SOSO)
*DatasetsApi* | [**datasets_soso_stream_get**](./DatasetsApi.md#datasets_soso_stream_get) | **GET** /datasets/SOSO/stream | SO-SO prices (SOSO) stream
*DatasetsApi* | [**datasets_syswarn_get**](./DatasetsApi.md#datasets_syswarn_get) | **GET** /datasets/SYSWARN | System warnings (SYSWARN)
*DatasetsApi* | [**datasets_syswarn_stream_get**](./DatasetsApi.md#datasets_syswarn_stream_get) | **GET** /datasets/SYSWARN/stream | System warnings (SYSWARN) stream
*DatasetsApi* | [**datasets_temp_get**](./DatasetsApi.md#datasets_temp_get) | **GET** /datasets/TEMP | Temperature data (TEMP)
*DatasetsApi* | [**datasets_tsdf_get**](./DatasetsApi.md#datasets_tsdf_get) | **GET** /datasets/TSDF | Day and day-ahead Transmission System Demand forecast (TSDF)
*DatasetsApi* | [**datasets_tsdf_stream_get**](./DatasetsApi.md#datasets_tsdf_stream_get) | **GET** /datasets/TSDF/stream | Day and day-ahead Transmission System Demand forecast (TSDF) stream
*DatasetsApi* | [**datasets_tsdfd_get**](./DatasetsApi.md#datasets_tsdfd_get) | **GET** /datasets/TSDFD | 2-14 days ahead Transmission System Demand and surplus forecast (TSDFD)
*DatasetsApi* | [**datasets_tsdfd_stream_get**](./DatasetsApi.md#datasets_tsdfd_stream_get) | **GET** /datasets/TSDFD/stream | 2-14 days ahead Transmission System Demand and surplus forecast (TSDFD) stream
*DatasetsApi* | [**datasets_tsdfw_get**](./DatasetsApi.md#datasets_tsdfw_get) | **GET** /datasets/TSDFW | 2-52 weeks ahead Transmission System Demand and surplus forecast (TSDFW)
*DatasetsApi* | [**datasets_tsdfw_stream_get**](./DatasetsApi.md#datasets_tsdfw_stream_get) | **GET** /datasets/TSDFW/stream | 2-52 weeks ahead Transmission System Demand and surplus forecast (TSDFW) stream
*DatasetsApi* | [**datasets_tudm_get**](./DatasetsApi.md#datasets_tudm_get) | **GET** /datasets/TUDM | Trading unit data (S0491_TUDM)
*DatasetsApi* | [**datasets_tudm_stream_get**](./DatasetsApi.md#datasets_tudm_stream_get) | **GET** /datasets/TUDM/stream | Trading unit data (S0491_TUDM) stream
*DatasetsApi* | [**datasets_uou2_t14_d_get**](./DatasetsApi.md#datasets_uou2_t14_d_get) | **GET** /datasets/UOU2T14D | 2 to 14 days ahead generation availability aggregated by Balancing Mechanism Units (UOU2T14D)
*DatasetsApi* | [**datasets_uou2_t14_d_stream_get**](./DatasetsApi.md#datasets_uou2_t14_d_stream_get) | **GET** /datasets/UOU2T14D/stream | 2 to 14 days ahead generation availability aggregated by Balancing Mechanism Units (UOU2T14D) stream
*DatasetsApi* | [**datasets_uou2_t3_yw_get**](./DatasetsApi.md#datasets_uou2_t3_yw_get) | **GET** /datasets/UOU2T3YW | 2 to 156 weeks ahead generation availability aggregated by Balancing Mechanism Units (UOU2T3YW)
*DatasetsApi* | [**datasets_uou2_t3_yw_stream_get**](./DatasetsApi.md#datasets_uou2_t3_yw_stream_get) | **GET** /datasets/UOU2T3YW/stream | 2 to 156 weeks ahead generation availability aggregated by Balancing Mechanism Units (UOU2T3YW) stream
*DatasetsApi* | [**datasets_watl_get**](./DatasetsApi.md#datasets_watl_get) | **GET** /datasets/WATL | Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630)
*DatasetsApi* | [**datasets_watl_stream_get**](./DatasetsApi.md#datasets_watl_stream_get) | **GET** /datasets/WATL/stream | Week-Ahead Total Load Forecast Per Bidding Zone (WATL / B0630) stream
*DatasetsApi* | [**datasets_windfor_get**](./DatasetsApi.md#datasets_windfor_get) | **GET** /datasets/WINDFOR | Wind generation forecast (WINDFOR)
*DatasetsApi* | [**datasets_windfor_stream_get**](./DatasetsApi.md#datasets_windfor_stream_get) | **GET** /datasets/WINDFOR/stream | Wind generation forecast (WINDFOR) stream
*DatasetsApi* | [**datasets_yafm_get**](./DatasetsApi.md#datasets_yafm_get) | **GET** /datasets/YAFM | Year Ahead Forecast Margin (YAFM / B0810)
*DatasetsApi* | [**datasets_yafm_stream_get**](./DatasetsApi.md#datasets_yafm_stream_get) | **GET** /datasets/YAFM/stream | Year Ahead Forecast Margin (YAFM / B0810) stream
*DatasetsApi* | [**datasets_yatl_get**](./DatasetsApi.md#datasets_yatl_get) | **GET** /datasets/YATL | Year-Ahead Total Load Forecast Per Bidding Zone (YATL / B0650)
*DatasetsApi* | [**datasets_yatl_stream_get**](./DatasetsApi.md#datasets_yatl_stream_get) | **GET** /datasets/YATL/stream | Year-Ahead Total Load Forecast Per Bidding Zone (YATL / B0650) stream
*DemandApi* | [**demand_actual_total_get**](./DemandApi.md#demand_actual_total_get) | **GET** /demand/actual/total | Actual total load (ATL/B0610)
*DemandApi* | [**demand_get**](./DemandApi.md#demand_get) | **GET** /demand | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_outturn_daily_get**](./DemandApi.md#demand_outturn_daily_get) | **GET** /demand/outturn/daily | Initial National Demand outturn per day (INDOD)
*DemandApi* | [**demand_outturn_daily_stream_get**](./DemandApi.md#demand_outturn_daily_stream_get) | **GET** /demand/outturn/daily/stream | Initial National Demand outturn per day (INDOD) stream
*DemandApi* | [**demand_outturn_get**](./DemandApi.md#demand_outturn_get) | **GET** /demand/outturn | Initial National Demand outturn (INDO)
*DemandApi* | [**demand_outturn_stream_get**](./DemandApi.md#demand_outturn_stream_get) | **GET** /demand/outturn/stream | Initial National Demand outturn (INDO) stream
*DemandApi* | [**demand_outturn_summary_get**](./DemandApi.md#demand_outturn_summary_get) | **GET** /demand/outturn/summary | System demand summary (FUELINST)
*DemandApi* | [**demand_peak_get**](./DemandApi.md#demand_peak_get) | **GET** /demand/peak | Peak demand per day (ITSDO)
*DemandApi* | [**demand_peak_indicative_get**](./DemandApi.md#demand_peak_indicative_get) | **GET** /demand/peak/indicative | Indicative peak demand per day (S0142, ITSDO, FUELHH)
*DemandApi* | [**demand_peak_indicative_operational_triad_season_get**](./DemandApi.md#demand_peak_indicative_operational_triad_season_get) | **GET** /demand/peak/indicative/operational/{triadSeason} | Operational data demand peaks for a Triad season (ITSDO, FUELHH)
*DemandApi* | [**demand_peak_indicative_settlement_triad_season_get**](./DemandApi.md#demand_peak_indicative_settlement_triad_season_get) | **GET** /demand/peak/indicative/settlement/{triadSeason} | Settlement data demand peaks for a Triad season (S0142)
*DemandApi* | [**demand_peak_triad_get**](./DemandApi.md#demand_peak_triad_get) | **GET** /demand/peak/triad | Triad demand peaks (S0142, ITSDO, FUELHH)
*DemandApi* | [**demand_rolling_system_demand_get**](./DemandApi.md#demand_rolling_system_demand_get) | **GET** /demand/rollingSystemDemand | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_stream_get**](./DemandApi.md#demand_stream_get) | **GET** /demand/stream | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_summary_get**](./DemandApi.md#demand_summary_get) | **GET** /demand/summary | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandApi* | [**demand_total_actual_get**](./DemandApi.md#demand_total_actual_get) | **GET** /demand/total/actual | This endpoint is obsolete, and this location may be removed with no further notice.
*DemandForecastApi* | [**forecast_demand_daily_evolution_get**](./DemandForecastApi.md#forecast_demand_daily_evolution_get) | **GET** /forecast/demand/daily/evolution | Evolution of the fourteen-day demand forecast over time (NDFD, TSDFD)
*DemandForecastApi* | [**forecast_demand_daily_get**](./DemandForecastApi.md#forecast_demand_daily_get) | **GET** /forecast/demand/daily | Fourteen day demand forecast (NDFD, TSDFD)
*DemandForecastApi* | [**forecast_demand_daily_history_get**](./DemandForecastApi.md#forecast_demand_daily_history_get) | **GET** /forecast/demand/daily/history | History of the fourteen-day demand forecast (NDFD, TSDFD)
*DemandForecastApi* | [**forecast_demand_day_ahead_earliest_get**](./DemandForecastApi.md#forecast_demand_day_ahead_earliest_get) | **GET** /forecast/demand/day-ahead/earliest | Historic view of the earliest forecasted demand (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_earliest_stream_get**](./DemandForecastApi.md#forecast_demand_day_ahead_earliest_stream_get) | **GET** /forecast/demand/day-ahead/earliest/stream | Historic view of the earliest forecasted demand (NDF, TSDF) stream
*DemandForecastApi* | [**forecast_demand_day_ahead_evolution_get**](./DemandForecastApi.md#forecast_demand_day_ahead_evolution_get) | **GET** /forecast/demand/day-ahead/evolution | Evolution of the day-ahead demand forecast over time (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_get**](./DemandForecastApi.md#forecast_demand_day_ahead_get) | **GET** /forecast/demand/day-ahead | Day-ahead demand forecast (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_history_get**](./DemandForecastApi.md#forecast_demand_day_ahead_history_get) | **GET** /forecast/demand/day-ahead/history | History of the day-ahead demand forecast (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_latest_get**](./DemandForecastApi.md#forecast_demand_day_ahead_latest_get) | **GET** /forecast/demand/day-ahead/latest | Historic view of the latest forecasted demand (NDF, TSDF)
*DemandForecastApi* | [**forecast_demand_day_ahead_latest_stream_get**](./DemandForecastApi.md#forecast_demand_day_ahead_latest_stream_get) | **GET** /forecast/demand/day-ahead/latest/stream | Historic view of the latest forecasted demand (NDF, TSDF) stream
*DemandForecastApi* | [**forecast_demand_day_ahead_peak_get**](./DemandForecastApi.md#forecast_demand_day_ahead_peak_get) | **GET** /forecast/demand/day-ahead/peak | Peak forecasted demand per day (TSDF)
*DemandForecastApi* | [**forecast_demand_total_day_ahead_get**](./DemandForecastApi.md#forecast_demand_total_day_ahead_get) | **GET** /forecast/demand/total/day-ahead | Day-ahead total load forecast (DATL/B0620)
*DemandForecastApi* | [**forecast_demand_total_week_ahead_get**](./DemandForecastApi.md#forecast_demand_total_week_ahead_get) | **GET** /forecast/demand/total/week-ahead | Week-ahead total load forecast (WATL/B0630)
*DemandForecastApi* | [**forecast_demand_total_week_ahead_latest_get**](./DemandForecastApi.md#forecast_demand_total_week_ahead_latest_get) | **GET** /forecast/demand/total/week-ahead/latest | Latest week-ahead total load forecast (WATL/B0630)
*DemandForecastApi* | [**forecast_demand_weekly_evolution_get**](./DemandForecastApi.md#forecast_demand_weekly_evolution_get) | **GET** /forecast/demand/weekly/evolution | Evolution of the one-year demand forecast over time  (NDFW, TSDFW)
*DemandForecastApi* | [**forecast_demand_weekly_get**](./DemandForecastApi.md#forecast_demand_weekly_get) | **GET** /forecast/demand/weekly | One-year demand forecast (NDFW, TSDFW)
*DemandForecastApi* | [**forecast_demand_weekly_history_get**](./DemandForecastApi.md#forecast_demand_weekly_history_get) | **GET** /forecast/demand/weekly/history | History of the one-year demand forecast (NDFW, TSDFW)
*GenerationApi* | [**generation_actual_per_type_day_total_get**](./GenerationApi.md#generation_actual_per_type_day_total_get) | **GET** /generation/actual/per-type/day-total | Current snapshot of actual generation by fuel type categories (AGPT/B1620)
*GenerationApi* | [**generation_actual_per_type_get**](./GenerationApi.md#generation_actual_per_type_get) | **GET** /generation/actual/per-type | Historic actual generation automatically down-sampled (AGPT/B1620)
*GenerationApi* | [**generation_actual_per_type_wind_and_solar_get**](./GenerationApi.md#generation_actual_per_type_wind_and_solar_get) | **GET** /generation/actual/per-type/wind-and-solar | Historic actual or estimated wind and solar power generation (AGWS/B1630)
*GenerationApi* | [**generation_outturn_current_get**](./GenerationApi.md#generation_outturn_current_get) | **GET** /generation/outturn/current | Current snapshot of generation by fuel type categories (FUELINST, FUELHH)
*GenerationApi* | [**generation_outturn_fuelinsthhcur_get**](./GenerationApi.md#generation_outturn_fuelinsthhcur_get) | **GET** /generation/outturn/FUELINSTHHCUR | This endpoint is obsolete, and this location may be removed with no further notice.
*GenerationApi* | [**generation_outturn_get**](./GenerationApi.md#generation_outturn_get) | **GET** /generation/outturn | Total generation outturn (FUELINST)
*GenerationApi* | [**generation_outturn_half_hourly_interconnector_get**](./GenerationApi.md#generation_outturn_half_hourly_interconnector_get) | **GET** /generation/outturn/halfHourlyInterconnector | This endpoint is obsolete, and this location may be removed with no further notice.
*GenerationApi* | [**generation_outturn_interconnectors_get**](./GenerationApi.md#generation_outturn_interconnectors_get) | **GET** /generation/outturn/interconnectors | Historic half-hourly interconnector flows (FUELINST)
*GenerationApi* | [**generation_outturn_summary_get**](./GenerationApi.md#generation_outturn_summary_get) | **GET** /generation/outturn/summary | Historic generation automatically down-sampled (FUELINST)
*GenerationForecastApi* | [**forecast_availability_daily_evolution_get**](./GenerationForecastApi.md#forecast_availability_daily_evolution_get) | **GET** /forecast/availability/daily/evolution | Evolution of the fourteen-day generation capacity forecast over time (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_daily_get**](./GenerationForecastApi.md#forecast_availability_daily_get) | **GET** /forecast/availability/daily | Fourteen-day generation capacity forecast (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_daily_history_get**](./GenerationForecastApi.md#forecast_availability_daily_history_get) | **GET** /forecast/availability/daily/history | History of the fourteen-day generation capacity forecast (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_summary14_d_get**](./GenerationForecastApi.md#forecast_availability_summary14_d_get) | **GET** /forecast/availability/summary/14D | Down-sampled fourteen-day generation forecast (FOU2T14D)
*GenerationForecastApi* | [**forecast_availability_summary3_yw_get**](./GenerationForecastApi.md#forecast_availability_summary3_yw_get) | **GET** /forecast/availability/summary/3YW | Down-sampled three-year generation forecast (FOU2T3YW)
*GenerationForecastApi* | [**forecast_availability_weekly_evolution_get**](./GenerationForecastApi.md#forecast_availability_weekly_evolution_get) | **GET** /forecast/availability/weekly/evolution | Evolution of the three-year generation capacity forecast over time (FOU2T3YW)
*GenerationForecastApi* | [**forecast_availability_weekly_get**](./GenerationForecastApi.md#forecast_availability_weekly_get) | **GET** /forecast/availability/weekly | Three-year generation capacity forecast (FOU2T3YW)
*GenerationForecastApi* | [**forecast_availability_weekly_history_get**](./GenerationForecastApi.md#forecast_availability_weekly_history_get) | **GET** /forecast/availability/weekly/history | History of the three-year generation capacity forecast (FOU2T3YW)
*GenerationForecastApi* | [**forecast_generation_day_ahead_get**](./GenerationForecastApi.md#forecast_generation_day_ahead_get) | **GET** /forecast/generation/day-ahead | Day-ahead aggregated generation (DAG/B1430)
*GenerationForecastApi* | [**forecast_generation_wind_and_solar_day_ahead_get**](./GenerationForecastApi.md#forecast_generation_wind_and_solar_day_ahead_get) | **GET** /forecast/generation/wind-and-solar/day-ahead | Day-ahead generation forecast for wind and solar (DGWS/B1440)
*GenerationForecastApi* | [**forecast_generation_wind_earliest_get**](./GenerationForecastApi.md#forecast_generation_wind_earliest_get) | **GET** /forecast/generation/wind/earliest | Historic view of the earliest forecasted wind generation (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_earliest_stream_get**](./GenerationForecastApi.md#forecast_generation_wind_earliest_stream_get) | **GET** /forecast/generation/wind/earliest/stream | Historic view of the earliest forecasted wind generation (WINDFOR) stream
*GenerationForecastApi* | [**forecast_generation_wind_evolution_get**](./GenerationForecastApi.md#forecast_generation_wind_evolution_get) | **GET** /forecast/generation/wind/evolution | Evolution of the wind generation forecast over time (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_get**](./GenerationForecastApi.md#forecast_generation_wind_get) | **GET** /forecast/generation/wind | Current wind generation forecast (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_history_get**](./GenerationForecastApi.md#forecast_generation_wind_history_get) | **GET** /forecast/generation/wind/history | History of the wind generation forecast (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_latest_get**](./GenerationForecastApi.md#forecast_generation_wind_latest_get) | **GET** /forecast/generation/wind/latest | Historic view of the latest forecasted wind generation (WINDFOR)
*GenerationForecastApi* | [**forecast_generation_wind_latest_stream_get**](./GenerationForecastApi.md#forecast_generation_wind_latest_stream_get) | **GET** /forecast/generation/wind/latest/stream | Historic view of the latest forecasted wind generation (WINDFOR) stream
*GenerationForecastApi* | [**forecast_generation_wind_peak_get**](./GenerationForecastApi.md#forecast_generation_wind_peak_get) | **GET** /forecast/generation/wind/peak | Peak wind generation forecast for each day (WINDFOR)
*HealthCheckApi* | [**health_get**](./HealthCheckApi.md#health_get) | **GET** /health | Health check
*IndicatedForecastApi* | [**forecast_indicated_day_ahead_evolution_get**](./IndicatedForecastApi.md#forecast_indicated_day_ahead_evolution_get) | **GET** /forecast/indicated/day-ahead/evolution | Evolution indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
*IndicatedForecastApi* | [**forecast_indicated_day_ahead_get**](./IndicatedForecastApi.md#forecast_indicated_day_ahead_get) | **GET** /forecast/indicated/day-ahead | Latest indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
*IndicatedForecastApi* | [**forecast_indicated_day_ahead_history_get**](./IndicatedForecastApi.md#forecast_indicated_day_ahead_history_get) | **GET** /forecast/indicated/day-ahead/history | Historical indicated day-ahead forecast (INDDEM, INDGEN, IMBALNGC, MELNGC)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_get) | **GET** /balancing/settlement/acceptance/volumes/all/{bidOffer}/{settlementDate} | Acceptance volumes by settlement date (BOAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_acceptance_volumes_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/acceptance/volumes/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Acceptance volumes by settlement period (BOAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_acceptances_all_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_acceptances_all_settlement_date_settlement_period_get) | **GET** /balancing/settlement/acceptances/all/{settlementDate}/{settlementPeriod} | Historic acceptances by settlement period (ISPSTACK, BOALF, BOD)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_default_notices_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_default_notices_get) | **GET** /balancing/settlement/default-notices | Default notices (CDN)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_get) | **GET** /balancing/settlement/indicative/cashflows/all/{bidOffer}/{settlementDate} | Indicative period BMU cashflows by settlement date (EBOCF)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_cashflows_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/indicative/cashflows/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Indicative period BMU cashflows by settlement period (EBOCF)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_get) | **GET** /balancing/settlement/indicative/volumes/all/{bidOffer}/{settlementDate} | Indicative volumes by settlement date (DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_indicative_volumes_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/indicative/volumes/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Indicative volumes by settlement period (DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_market_depth_settlement_date_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_market_depth_settlement_date_get) | **GET** /balancing/settlement/market-depth/{settlementDate} | Market depth by settlement date (IMBALNGC, BOD, DISEBSP, DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_market_depth_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_market_depth_settlement_date_settlement_period_get) | **GET** /balancing/settlement/market-depth/{settlementDate}/{settlementPeriod} | Market depth by settlement period (IMBALNGC, BOD, DISEBSP, DISPTAV)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_messages_settlement_date_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_messages_settlement_date_get) | **GET** /balancing/settlement/messages/{settlementDate} | Settlement messages by settlement date (SMSG)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_messages_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_messages_settlement_date_settlement_period_get) | **GET** /balancing/settlement/messages/{settlementDate}/{settlementPeriod} | Settlement messages by settlement date and period (SMSG)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_stack_all_bid_offer_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_stack_all_bid_offer_settlement_date_settlement_period_get) | **GET** /balancing/settlement/stack/all/{bidOffer}/{settlementDate}/{settlementPeriod} | Settlement bid-offer stacks by settlement period (ISPSTACK)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_summary_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_summary_settlement_date_settlement_period_get) | **GET** /balancing/settlement/summary/{settlementDate}/{settlementPeriod} | Settlement calculation summary (ISPSTACK, DISEBSP, MID, NETBSAD)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_system_prices_settlement_date_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_system_prices_settlement_date_get) | **GET** /balancing/settlement/system-prices/{settlementDate} | Settlement system prices by settlement date (DISEBSP)
*IndicativeImbalanceSettlementApi* | [**balancing_settlement_system_prices_settlement_date_settlement_period_get**](./IndicativeImbalanceSettlementApi.md#balancing_settlement_system_prices_settlement_date_settlement_period_get) | **GET** /balancing/settlement/system-prices/{settlementDate}/{settlementPeriod} | Settlement system prices by settlement date and period (DISEBSP)
*LegacyApi* | [**interop_message_detail_retrieval_get**](./LegacyApi.md#interop_message_detail_retrieval_get) | **GET** /interop/MessageDetailRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
*LegacyApi* | [**interop_message_list_retrieval_get**](./LegacyApi.md#interop_message_list_retrieval_get) | **GET** /interop/MessageListRetrieval | This endpoint is obsolete, and this location may be removed with no further notice. Use /remit/* or /datasets/REMIT endpoints instead.
*LossOfLoadProbabilityAndDeRatedMarginApi* | [**lolpdrm_forecast_evolution_get**](./LossOfLoadProbabilityAndDeRatedMarginApi.md#lolpdrm_forecast_evolution_get) | **GET** /lolpdrm/forecast/evolution | Loss of load probability and de-rated margin forecast (LOLPDRM)
*MarginForecastApi* | [**forecast_margin_daily_evolution_get**](./MarginForecastApi.md#forecast_margin_daily_evolution_get) | **GET** /forecast/margin/daily/evolution | Evolution daily margin forecast (OCNMFD2)
*MarginForecastApi* | [**forecast_margin_daily_get**](./MarginForecastApi.md#forecast_margin_daily_get) | **GET** /forecast/margin/daily | Daily margin forecast (OCNMFD2)
*MarginForecastApi* | [**forecast_margin_daily_history_get**](./MarginForecastApi.md#forecast_margin_daily_history_get) | **GET** /forecast/margin/daily/history | Historical daily margin forecast (OCNMFD2)
*MarginForecastApi* | [**forecast_margin_weekly_evolution_get**](./MarginForecastApi.md#forecast_margin_weekly_evolution_get) | **GET** /forecast/margin/weekly/evolution | Evolution daily margin forecast (OCNMFW2, OCNMF3Y2)
*MarginForecastApi* | [**forecast_margin_weekly_get**](./MarginForecastApi.md#forecast_margin_weekly_get) | **GET** /forecast/margin/weekly | Weekly margin forecast (OCNMFW2, OCNMF3Y2)
*MarginForecastApi* | [**forecast_margin_weekly_history_get**](./MarginForecastApi.md#forecast_margin_weekly_history_get) | **GET** /forecast/margin/weekly/history | Historical weekly margin forecast (OCNMFW2, OCNMF3Y2)
*MarketIndexApi* | [**balancing_pricing_market_index_get**](./MarketIndexApi.md#balancing_pricing_market_index_get) | **GET** /balancing/pricing/market-index | Market Index Data (MID) price time series
*NonBMSTORApi* | [**balancing_nonbm_stor_events_get**](./NonBMSTORApi.md#balancing_nonbm_stor_events_get) | **GET** /balancing/nonbm/stor/events | Non-BM STOR events (NONBM)
*NonBMSTORApi* | [**balancing_nonbm_stor_get**](./NonBMSTORApi.md#balancing_nonbm_stor_get) | **GET** /balancing/nonbm/stor | Non-BM STOR time series (NONBM)
*NonBMVolumesApi* | [**balancing_nonbm_volumes_get**](./NonBMVolumesApi.md#balancing_nonbm_volumes_get) | **GET** /balancing/nonbm/volumes | Balancing services volume (QAS)
*REMITApi* | [**remit_get**](./REMITApi.md#remit_get) | **GET** /remit | Bulk fetch message details by IDs
*REMITApi* | [**remit_list_by_event_get**](./REMITApi.md#remit_list_by_event_get) | **GET** /remit/list/by-event | List messages by event time
*REMITApi* | [**remit_list_by_event_stream_get**](./REMITApi.md#remit_list_by_event_stream_get) | **GET** /remit/list/by-event/stream | List messages by event time (stream)
*REMITApi* | [**remit_list_by_publish_get**](./REMITApi.md#remit_list_by_publish_get) | **GET** /remit/list/by-publish | List messages by publish time
*REMITApi* | [**remit_list_by_publish_stream_get**](./REMITApi.md#remit_list_by_publish_stream_get) | **GET** /remit/list/by-publish/stream | List messages by publish time (stream)
*REMITApi* | [**remit_message_id_get**](./REMITApi.md#remit_message_id_get) | **GET** /remit/{messageId} | Fetch message details by ID
*REMITApi* | [**remit_revisions_get**](./REMITApi.md#remit_revisions_get) | **GET** /remit/revisions | List all message revisions
*REMITApi* | [**remit_search_get**](./REMITApi.md#remit_search_get) | **GET** /remit/search | Fetch message details by mRID
*ReferenceApi* | [**reference_bmunits_all_get**](./ReferenceApi.md#reference_bmunits_all_get) | **GET** /reference/bmunits/all | BM Units
*ReferenceApi* | [**reference_fueltypes_all_get**](./ReferenceApi.md#reference_fueltypes_all_get) | **GET** /reference/fueltypes/all | Fuel types
*ReferenceApi* | [**reference_interconnectors_all_get**](./ReferenceApi.md#reference_interconnectors_all_get) | **GET** /reference/interconnectors/all | Interconnectors
*ReferenceApi* | [**reference_remit_assets_all_get**](./ReferenceApi.md#reference_remit_assets_all_get) | **GET** /reference/remit/assets/all | Assets
*ReferenceApi* | [**reference_remit_fueltypes_all_get**](./ReferenceApi.md#reference_remit_fueltypes_all_get) | **GET** /reference/remit/fueltypes/all | REMIT fuel types
*ReferenceApi* | [**reference_remit_participants_all_get**](./ReferenceApi.md#reference_remit_participants_all_get) | **GET** /reference/remit/participants/all | Participants
*RollingSystemDemandApi* | [**generation_outturn_get**](./RollingSystemDemandApi.md#generation_outturn_get) | **GET** /generation/outturn | Total generation outturn (FUELINST)
*SOSOPricesApi* | [**soso_prices_get**](./SOSOPricesApi.md#soso_prices_get) | **GET** /soso/prices | SO-SO prices (SOSO)
*SurplusForecastApi* | [**forecast_surplus_daily_evolution_get**](./SurplusForecastApi.md#forecast_surplus_daily_evolution_get) | **GET** /forecast/surplus/daily/evolution | Evolution daily surplus forecast (OCNMFD)
*SurplusForecastApi* | [**forecast_surplus_daily_get**](./SurplusForecastApi.md#forecast_surplus_daily_get) | **GET** /forecast/surplus/daily | Daily surplus forecast (OCNMFD)
*SurplusForecastApi* | [**forecast_surplus_daily_history_get**](./SurplusForecastApi.md#forecast_surplus_daily_history_get) | **GET** /forecast/surplus/daily/history | Historical daily surplus forecast (OCNMFD)
*SurplusForecastApi* | [**forecast_surplus_weekly_evolution_get**](./SurplusForecastApi.md#forecast_surplus_weekly_evolution_get) | **GET** /forecast/surplus/weekly/evolution | Evolution weekly surplus forecast (OCNMFW, OCNMF3Y)
*SurplusForecastApi* | [**forecast_surplus_weekly_get**](./SurplusForecastApi.md#forecast_surplus_weekly_get) | **GET** /forecast/surplus/weekly | Weekly surplus forecast (OCNMFW, OCNMF3Y)
*SurplusForecastApi* | [**forecast_surplus_weekly_history_get**](./SurplusForecastApi.md#forecast_surplus_weekly_history_get) | **GET** /forecast/surplus/weekly/history | Historical weekly surplus forecast (OCNMFW, OCNMF3Y)
*SystemApi* | [**system_demand_control_instructions_get**](./SystemApi.md#system_demand_control_instructions_get) | **GET** /system/demand-control-instructions | Demand control instructions (DCI)
*SystemApi* | [**system_frequency_get**](./SystemApi.md#system_frequency_get) | **GET** /system/frequency | System frequency (FREQ)
*SystemApi* | [**system_frequency_stream_get**](./SystemApi.md#system_frequency_stream_get) | **GET** /system/frequency/stream | System frequency (FREQ) stream
*SystemApi* | [**system_warnings_get**](./SystemApi.md#system_warnings_get) | **GET** /system/warnings | System warnings (SYSWARN)
*SystemForecastApi* | [**forecast_system_loss_of_load_get**](./SystemForecastApi.md#forecast_system_loss_of_load_get) | **GET** /forecast/system/loss-of-load | Loss of load probability and de-rated margin forecast (LOLPDRM)
*TemperatureApi* | [**temperature_get**](./TemperatureApi.md#temperature_get) | **GET** /temperature | Temperature data (TEMP)
